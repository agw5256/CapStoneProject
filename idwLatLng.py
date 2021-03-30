# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



# Press the green button in the gutter to run the script.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import tensorflow as tf


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
url = []
url.append('/Users/agw52/PycharmProjects/pythonidw200601/2006년01분기평균위경도.xlsx')
url.append('/Users/agw52/PycharmProjects/pythonidw200601/2006년02분기평균위경도.xlsx')
url.append('/Users/agw52/PycharmProjects/pythonidw200601/2006년03분기평균위경도.xlsx')
url.append('/Users/agw52/PycharmProjects/pythonidw200601/2006년04분기평균위경도.xlsx')
url.append('/Users/agw52/PycharmProjects/pythonidw200601/2007년01분기평균위경도.xlsx')
url.append('/Users/agw52/PycharmProjects/pythonidw200601/2007년02분기평균위경도.xlsx')
url.append('/Users/agw52/PycharmProjects/pythonidw200601/2007년03분기평균위경도.xlsx')
url.append('/Users/agw52/PycharmProjects/pythonidw200601/2007년04분기평균위경도.xlsx')
url.append('/Users/agw52/PycharmProjects/pythonidw200601/2008년01분기평균위경도.xlsx')
url.append('/Users/agw52/PycharmProjects/pythonidw200601/2008년02분기평균위경도.xlsx')
url.append('/Users/agw52/PycharmProjects/pythonidw200601/2008년03분기평균위경도.xlsx')
url.append('/Users/agw52/PycharmProjects/pythonidw200601/2008년04분기평균위경도.xlsx')
url.append('/Users/agw52/PycharmProjects/pythonidw200601/2009년01분기평균위경도.xlsx')
url.append('/Users/agw52/PycharmProjects/pythonidw200601/2009년02분기평균위경도.xlsx')
url.append('/Users/agw52/PycharmProjects/pythonidw200601/2009년03분기평균위경도.xlsx')
url.append('/Users/agw52/PycharmProjects/pythonidw200601/2009년04분기평균위경도.xlsx')
url.append('/Users/agw52/PycharmProjects/pythonidw200601/2010년01분기평균위경도.xlsx')
url.append('/Users/agw52/PycharmProjects/pythonidw200601/2010년02분기평균위경도.xlsx')
url.append('/Users/agw52/PycharmProjects/pythonidw200601/2010년03분기평균위경도.xlsx')
url.append('/Users/agw52/PycharmProjects/pythonidw200601/2010년04분기평균위경도.xlsx')

url1 = []
url1.append('/Users/agw52/PycharmProjects/pythonidw200601/2006년01분기평균위경도idw.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonidw200601/2006년02분기평균위경도idw.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonidw200601/2006년03분기평균위경도idw.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonidw200601/2006년04분기평균위경도idw.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonidw200601/2007년01분기평균위경도idw.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonidw200601/2007년02분기평균위경도idw.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonidw200601/2007년03분기평균위경도idw.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonidw200601/2007년04분기평균위경도idw.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonidw200601/2008년01분기평균위경도idw.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonidw200601/2008년02분기평균위경도idw.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonidw200601/2008년03분기평균위경도idw.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonidw200601/2008년04분기평균위경도idw.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonidw200601/2009년01분기평균위경도idw.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonidw200601/2009년02분기평균위경도idw.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonidw200601/2009년03분기평균위경도idw.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonidw200601/2009년04분기평균위경도idw.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonidw200601/2010년01분기평균위경도idw.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonidw200601/2010년02분기평균위경도idw.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonidw200601/2010년03분기평균위경도idw.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonidw200601/2010년04분기평균위경도idw.xlsx')

for all in range(len(url)):
    sample_1 = pd.read_excel(url[all], 'Sheet1')
    sample_2 = sample_1['위도']
    sample_3 = sample_1['경도']
    sample_4 = sample_1['PM10']
    sample_5 = sample_1['측정일시']
    sample_6 = sample_1['측정일시']
    sample_6 = sample_6.drop_duplicates(keep='first')
    totaldate = []

    for key in sample_6:
        print(key)
        totaldate.append(key)

    print(totaldate)

    x = []
    y = []
    z = []
    date = []
    for i in range(len(sample_1)):
        x.append(sample_2[i])
        y.append(sample_3[i])
        z.append(sample_4[i])
        date.append(sample_5[i])
    #print(x)
    #print(y)
    #print(z)
    #print(date)
    x1 = []
    y1 = []
    z1 = []
    for i in range(len(totaldate)):
        line1 = []
        line2 = []
        line3 = []
        for j in range(2):
            line1.append(0)
            line2.append(0)
            line3.append(0)
        x1.append(line1)
        y1.append(line2)
        z1.append(line3)

    for i in range(len(totaldate)):
        for j in range(len(sample_1)):
            if totaldate[i] == date[j]:
                x1[i].append(x[j])
                y1[i].append(y[j])
                z1[i].append(z[j])
    for i in range(len(totaldate)):
        del x1[i][0]
        del x1[i][0]
        del y1[i][0]
        del y1[i][0]
        del z1[i][0]
        del z1[i][0]

    print(x1[10])
    print(y1[10])
    print(z1[10])
    print(totaldate[10])

    def harvesine(lon1, lat1, lon2, lat2):
        rad = math.pi / 180  # degree to radian
        R = 6378.1  # earth average radius at equador (km)
        dlon = (lon2 - lon1) * rad
        dlat = (lat2 - lat1) * rad
        a = (math.sin(dlat / 2)) ** 2 + math.cos(lat1 * rad) * \
            math.cos(lat2 * rad) * (math.sin(dlon / 2)) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        d = R * c
        return(d)

    def idwr(x, y, z, xi, yi):
        lstxyzi = []
        for p in range(len(xi)):
            lstdist = []
            for s in range(len(x)):
                d = (harvesine(x[s], y[s], xi[p], yi[p]))
                lstdist.append(d)
            sumsup = list((1 / np.power(lstdist, 2)))
            suminf = np.sum(sumsup)
            sumsup = np.sum(np.array(sumsup) * np.array(z))
            u = sumsup / suminf
            xyzi = [xi[p], yi[p], u]
            lstxyzi.append(xyzi)
        return(lstxyzi)

    xi = [35.001]
    yi = [128.4667505]
    k=idwr(x1[10], y1[10], z1[10],xi,yi)
    print(k[0][2])
    latlon_1 = pd.read_excel('/Users/agw52/PycharmProjects/pythonidw200601/lon.xlsx', 'Sheet1')
    latlon_2 = latlon_1['lat']
    latlon_3 = latlon_1['lon']

    #print(latlon_2)
    #print(latlon_3)
    result = pd.concat([latlon_2,latlon_3],axis=1)
    #dfk = pd.DataFrame({"20200101": k})
    #result = pd.concat([result, dfk],axis=1)
    #print(result)
    for i in range(len(totaldate)):
        k = []
        for j in range(len(latlon_1)):
            xi = [latlon_2[j]]
            yi = [latlon_3[j]]
            ki = idwr(x1[i], y1[i], z1[i], xi, yi)
            k.append(ki[0][2])
            k[j] = round(k[j])
            print(i, j, k[j])
        dfk = pd.DataFrame(data={totaldate[i]: k}, columns=[totaldate[i]])
        result = pd.concat([result, dfk],axis=1)
        print(result)
    print(result)
    result.to_excel(url1[all], sheet_name='Sheet1')



