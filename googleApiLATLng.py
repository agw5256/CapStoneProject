# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import googlemaps
url1 = []
"""
url1.append('/Users/agw52/PycharmProjects/pythonlonlat/2006년01분기평균.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonlonlat/2006년02분기평균.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonlonlat/2006년03분기평균.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonlonlat/2006년04분기평균.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonlonlat/2007년01분기평균.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonlonlat/2007년02분기평균.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonlonlat/2007년03분기평균.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonlonlat/2007년04분기평균.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonlonlat/2008년01분기평균.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonlonlat/2008년02분기평균.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonlonlat/2008년03분기평균.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonlonlat/2008년04분기평균.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonlonlat/2009년01분기평균.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonlonlat/2009년02분기평균.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonlonlat/2009년03분기평균.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonlonlat/2009년04분기평균.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonlonlat/2010년01분기평균.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonlonlat/2010년02분기평균.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonlonlat/2010년03분기평균.xlsx')
"""
url1.append('/Users/agw52/PycharmProjects/pythonlonlat/2010년04분기평균.xlsx')

url2 = []
"""
url2.append('/Users/agw52/PycharmProjects/pythonlonlat/2006년01분기평균위경도.xlsx')
url2.append('/Users/agw52/PycharmProjects/pythonlonlat/2006년02분기평균위경도.xlsx')
url2.append('/Users/agw52/PycharmProjects/pythonlonlat/2006년03분기평균위경도.xlsx')
url2.append('/Users/agw52/PycharmProjects/pythonlonlat/2006년04분기평균위경도.xlsx')
url2.append('/Users/agw52/PycharmProjects/pythonlonlat/2007년01분기평균위경도.xlsx')
url2.append('/Users/agw52/PycharmProjects/pythonlonlat/2007년02분기평균위경도.xlsx')
url2.append('/Users/agw52/PycharmProjects/pythonlonlat/2007년03분기평균위경도.xlsx')
url2.append('/Users/agw52/PycharmProjects/pythonlonlat/2007년04분기평균위경도.xlsx')
url2.append('/Users/agw52/PycharmProjects/pythonlonlat/2008년01분기평균위경도.xlsx')
url2.append('/Users/agw52/PycharmProjects/pythonlonlat/2008년02분기평균위경도.xlsx')
url2.append('/Users/agw52/PycharmProjects/pythonlonlat/2008년03분기평균위경도.xlsx')
url2.append('/Users/agw52/PycharmProjects/pythonlonlat/2008년04분기평균위경도.xlsx')
url2.append('/Users/agw52/PycharmProjects/pythonlonlat/2009년01분기평균위경도.xlsx')
url2.append('/Users/agw52/PycharmProjects/pythonlonlat/2009년02분기평균위경도.xlsx')
url2.append('/Users/agw52/PycharmProjects/pythonlonlat/2009년03분기평균위경도.xlsx')
url2.append('/Users/agw52/PycharmProjects/pythonlonlat/2009년04분기평균위경도.xlsx')
url2.append('/Users/agw52/PycharmProjects/pythonlonlat/2010년01분기평균위경도.xlsx')
url2.append('/Users/agw52/PycharmProjects/pythonlonlat/2010년02분기평균위경도.xlsx')
url2.append('/Users/agw52/PycharmProjects/pythonlonlat/2010년03분기평균위경도.xlsx')
"""
url2.append('/Users/agw52/PycharmProjects/pythonlonlat/2010년04분기평균위경도.xlsx')

for j in range(len(url1)):
    sample_1 = pd.read_excel(url1[j], 'Sheet1')
    #print(sample_1)
    sample_2 = sample_1['주소']
    sample_3 = sample_1['측정일시']
    sample_4 = sample_1['PM10']
    sample_5 = sample_2.drop_duplicates(keep='first')
    print(sample_5)
    gmaps = googlemaps.Client(key='AI')
    geocode_result1 = gmaps.geocode('세종특별자치시 보듬3로 114', language='ko')

    lat = {1:'a'}
    lng = {1:'a'}
    for key in sample_5:
        print(key)
        gmaps = googlemaps.Client(key='AI')
        geocode_result = gmaps.geocode(key, language='ko')
        try:
            lat[key] = geocode_result[0]["geometry"]["location"]["lat"]
            lng[key] = geocode_result[0]["geometry"]["location"]["lng"]
            lat[key] = round(lat[key], 5)
            lng[key] = round(lng[key], 5)
            print(lat[key])
            print(lat[key])
        except:
            print(key + "는 없습니다.")


    new= pd.DataFrame(columns=['주소', '측정일시', 'PM10', '위도', '경도'])
    for i in range(len(sample_1)):
        try:
            new = new.append({'주소': sample_2[i],'측정일시':sample_3[i], 'PM10': sample_4[i], '위도':lat[sample_2[i]],
                          '경도': lng[sample_2[i]]},ignore_index=True)
            print(new.loc[i])
        except:
            new = new.append({'주소': sample_2[i], '측정일시': sample_3[i], 'PM10': sample_4[i], '위도': np.nan,
                          '경도': np.nan}, ignore_index=True)
            print(new.loc[i])
    new = new.dropna()
    print(new)
    new.to_excel(url2[j], sheet_name='Sheet1')
