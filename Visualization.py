import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
matplotlib.use('PDF')


def makeGraph(composite, total):
    #Number of columns
    N = 69
    #Size of hole in the middle
    #Max height of a column, makes the radius bottom + max_height = 6
    max_height = 10

    # Splits circumference into N equal pieces, if you split each piece smaller than 2*pi/N then you have space in between the bars
    width = (2 * np.pi) / N

    #Sets the range of theta and splits it into an array of N elements, endpoint True includes the stop point and default is True
    theta = np.linspace(0.0 + width/2, 2* np.pi+width/2, N, endpoint=False)

    #Make all N columns random sizes multiplied by 4 to get range from 0-4 instead of 0-1
    totalradii = max_height*total
    yearsradii = np.zeros((69,8))
    for i in range(0,69):
        yearsradii[i] = totalradii[i]*composite[i]



    #Creates a plot of 1 row, 1 col, and position 1 (basically creates 1 square cell and plots within that)a
    f, ax = plt.subplots(1, subplot_kw=dict(polar=True), figsize = (10,6))

    #plots bars on the polar subplot
    bottomResF = 4
    bottomResR = bottomResF + yearsradii[:,0]
    bottomCommF = bottomResR + yearsradii[:,1]
    bottomCommR = bottomCommF + yearsradii[:,2]
    bottomIndF = bottomCommR + yearsradii[:,3]
    bottomIndR = bottomIndF + yearsradii[:,4]
    bottomTranF = bottomIndR + yearsradii[:,5]
    bottomTranR = bottomTranF + yearsradii[:,6]

    bar = ax.bar(theta, yearsradii[:,0], width=width, bottom=bottomResF, label='Residential (Fossil)', edgecolor = 'black')
    bar2 = ax.bar(theta, yearsradii[:,1], width = width, bottom = bottomResR, label='Residential (Renewable)', edgecolor = 'black')
    bar3 = ax.bar(theta, yearsradii[:,2], width = width, bottom = bottomCommF, label='Commercial (Fossil)', edgecolor = 'black')
    bar4 = ax.bar(theta, yearsradii[:,3], width = width, bottom = bottomCommR, label='Commercial (Renewable)', edgecolor = 'black')
    bar5 = ax.bar(theta, yearsradii[:,4], width = width, bottom = bottomIndF, label='Industry (Fossil)', edgecolor = 'black')
    bar6 = ax.bar(theta, yearsradii[:,5], width = width, bottom = bottomIndR, label='Industry (Renewable)', edgecolor = 'black')
    bar7 = ax.bar(theta, yearsradii[:,6], width = width, bottom = bottomTranF, label='Transportation (Fossil)', edgecolor = 'black')
    bar8 = ax.bar(theta, yearsradii[:,7], width = width, bottom = bottomTranR, label='Transportation (Renewable)', edgecolor = 'black')

    bars = [bar, bar2, bar3, bar4, bar5, bar6, bar7, bar8]

    #Zip ties the radii and bars together in order, sets each to a color and transparency level
    color = ['darkgreen','lime','purple','magenta','darkred','red','saddlebrown','brown']

    ax.set_xticklabels(['1949\n2017', '1957', '1966', '1975', '1983', '1992', '2000', '2009'])
    ax.set_yticklabels(['', '', '96', '193', '289', '385', '482\nBillion BTUs Per Person'])

    for b in range(0, len(bars)):
        for ba in bars[b]:
            ba.set_alpha(0.9)
            ba.set_facecolor(color[b])
    plt.grid('off')
    plt.axis('on')
    plt.title("BTU Energy Consumption Per Person in the US each Year by Sector and Source from 1949 to 2017")
    plt.legend(loc='lower right', bbox_to_anchor=(1.55,0.05))
    plt.savefig('figure1')
'''#Number of columns
    N = 80
    #Size of hole in the middle
    bottom = 2
    #Max height of a column, makes the radius bottom + max_height = 6
    max_height = 4

    #Sets the range of theta and splits it into an array of N elements, endpoint True includes the stop point and default is True
    theta = np.linspace(0.0, 2* np.pi, N, endpoint=False)

    #Make all N columns random sizes multiplied by 4 to get range from 0-4 instead of 0-1
    radii = max_height*np.random.rand(N)

    #Splits circumference into 80 equal pieces, if you split each piece smaller than 2*pi/N then you have space in between the bars
    width = (2*np.pi) / N

    #Creates a plot of 1 row, 1 col, and position 1 (basically creates 1 square cell and plots within that)a
    ax = plt.subplot(111, polar=True)

    #plots bars on the polar subplot
    bars = ax.bar(theta, radii, width=width, bottom=bottom)

    #Zip ties the radii and bars together in order, sets each to a color and transparency level
    for r, bar in zip(radii, bars):
        bar.set_facecolor(plt.cm.jet(r / 10.))
        bar.set_alpha(0.8)
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    plt.axis('off')
    plt.show()
'''




def dataManip():
    Residential = pd.read_csv('MER_T02_02.csv')
    Commercial = pd.read_csv('MER_T02_03.csv')
    Industrial = pd.read_csv('MER_T02_04.csv')
    Transportation = pd.read_csv('MER_T02_05.csv')
    Electrical = pd.read_csv('MER_T02_06.csv')
    Population = [325.15, 323.07, 320.74, 318.39, 316.06, 313.87, 311.58, 309.33, 306.77, 304.09, 301.23, 298.38, 295.52,
                  292.81, 290.11, 287.63, 284.97, 282.16, 279.04, 275.85, 272.65, 269.39, 266.28, 263.13, 259.92, 256.51,
                  252.98, 249.62, 246.82, 244.50, 242.29, 240.13, 237.92, 235.82, 233.79, 231.66, 229.47, 227.22, 225.06,
                  222.58, 220.24, 218.04, 215.97, 213.85, 211.91, 209.90, 207.66, 205.05, 202.68, 200.71, 198.71, 196.56,
                  194.30, 191.89, 189.24, 186.54, 183.69, 180.67, 177.83, 174.88, 171.98, 168.90, 165.93, 163.03, 160.18,
                  157.55, 154.88, 152.27, 149.19]

    sectors = [Residential, Commercial, Industrial, Transportation, Electrical]
    names = ['Residential', 'Commercial', 'Industrial', 'Transportation', 'Electric Power']
    arr = np.zeros((69, 8))
    e = np.zeros(69)
    dfe = sectors[4].loc[(sectors[4]['YYYYMM']%100 == 13)]
    dff = dfe.loc[(sectors[4]['Description'] == 'Total Fossil Fuels Consumed by the Electric Power Sector')]
    dff = np.array(dff['Value'])
    dfr = dfe.loc[(sectors[4]['Description'] == 'Total Renewable Energy Consumed by the Electric Power Sector')]
    dfr = np.array(dfr['Value'])

    for sect in range(0, len(sectors)-1):
        if sect == len(sectors)-1:
            df = sectors[sect].loc[(sectors[sect]['YYYYMM'] % 100 == 13)]
            Fossil = df.loc[(sectors[sect]['Description'] == 'Total Fossil Fuels Consumed by the %s Sector' % names[sect])]
            Renew = df.loc[(sectors[sect]['Description'] == 'Biomass Energy Consumed by the Transportation Sector' % names[sect])]
            E = df.loc[(sectors[sect]['Description'] == 'Electricity Retail Sales to the %s Sector' % names[sect])]
        else:
            df = sectors[sect].loc[(sectors[sect]['YYYYMM'] % 100 == 13)]
            Fossil = df.loc[(sectors[sect]['Description'] == 'Total Fossil Fuels Consumed by the %s Sector' % names[sect])]
            Renew = df.loc[(sectors[sect]['Description'] == 'Total Renewable Energy Consumed by the %s Sector' % names[sect])]
            E = df.loc[(sectors[sect]['Description'] == 'Electricity Retail Sales to the %s Sector' % names[sect])]
        i = 0
        for val in Fossil['Value']:
            arr[i][sect*2] = float(val)
            i +=1
        i = 0
        for val in Renew['Value']:
            arr[i][sect*2 + 1] = float(val)
            i +=1
        i=0
        for val in E['Value']:
            ratiof = float(dff[i])/(float(dff[i]) + float(dfr[i]))
            ratior = float(dfr[i])/(float(dff[i]) + float(dfr[i]))
            arr[i][sect*2 + 1] += ratior*float(val)
            arr[i][sect*2] += ratiof*float(val)
            i +=1
    total = np.zeros(69)
    #Get each sector's % contribution to total energy consumption each year
    for row in range(0,69):
        total[row] = np.sum(arr[row])/Population[row]
        sum = 0.0
        for j in range(0,8):
            sum += arr[row][j]
        arr[row] = [x/sum for x in arr[row]]
    max = np.amax(total)
    print(total)
    total = np.array([x/max for x in total])
    #Total is each year as a % of the max energy consumption year
    return arr, total


if __name__ == "__main__":
    arr, total = dataManip()
    makeGraph(arr, total)