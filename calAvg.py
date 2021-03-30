# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
url = []
url.append('/Users/agw52/PycharmProjects/pythonProject1/2006년01분기.xlsx')
url.append('/Users/agw52/PycharmProjects/pythonProject1/2006년02분기.xlsx')
url.append('/Users/agw52/PycharmProjects/pythonProject1/2006년03분기.xlsx')
url.append('/Users/agw52/PycharmProjects/pythonProject1/2006년04분기.xlsx')
url.append('/Users/agw52/PycharmProjects/pythonProject1/2007년01분기.xlsx')
url.append('/Users/agw52/PycharmProjects/pythonProject1/2007년02분기.xlsx')
url.append('/Users/agw52/PycharmProjects/pythonProject1/2007년03분기.xlsx')
url.append('/Users/agw52/PycharmProjects/pythonProject1/2007년04분기.xlsx')
url.append('/Users/agw52/PycharmProjects/pythonProject1/2008년01분기.xlsx')
url.append('/Users/agw52/PycharmProjects/pythonProject1/2008년02분기.xlsx')
url.append('/Users/agw52/PycharmProjects/pythonProject1/2008년03분기.xlsx')
url.append('/Users/agw52/PycharmProjects/pythonProject1/2008년04분기.xlsx')
url.append('/Users/agw52/PycharmProjects/pythonProject1/2009년01분기.xlsx')
url.append('/Users/agw52/PycharmProjects/pythonProject1/2009년02분기.xlsx')
url.append('/Users/agw52/PycharmProjects/pythonProject1/2009년03분기.xlsx')
url.append('/Users/agw52/PycharmProjects/pythonProject1/2009년04분기.xlsx')
url.append('/Users/agw52/PycharmProjects/pythonProject1/2010년01분기.xlsx')
url.append('/Users/agw52/PycharmProjects/pythonProject1/2010년02분기.xlsx')
url.append('/Users/agw52/PycharmProjects/pythonProject1/2010년03분기.xlsx')
url.append('/Users/agw52/PycharmProjects/pythonProject1/2010년04분기.xlsx')

url1 = []
url1.append('/Users/agw52/PycharmProjects/pythonProject1/2006년01분기평균.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonProject1/2006년02분기평균.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonProject1/2006년03분기평균.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonProject1/2006년04분기평균.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonProject1/2007년01분기평균.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonProject1/2007년02분기평균.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonProject1/2007년03분기평균.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonProject1/2007년04분기평균.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonProject1/2008년01분기평균.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonProject1/2008년02분기평균.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonProject1/2008년03분기평균.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonProject1/2008년04분기평균.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonProject1/2009년01분기평균.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonProject1/2009년02분기평균.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonProject1/2009년03분기평균.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonProject1/2009년04분기평균.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonProject1/2010년01분기평균.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonProject1/2010년02분기평균.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonProject1/2010년03분기평균.xlsx')
url1.append('/Users/agw52/PycharmProjects/pythonProject1/2010년04분기평균.xlsx')
print(len(url))
print(url[0])


for i in range(len(url)):
    sample_1 = pd.read_excel(url[i])
    print(sample_1)

    print(sample_1.columns)
    print(sample_1.dtypes)
    sample_1 = sample_1.drop(columns=['SO2'])
    sample_1 = sample_1.drop(columns=['CO'])
    sample_1 = sample_1.drop(columns=['O3'])
    sample_1 = sample_1.drop(columns=['NO2'])
    sample_1 = sample_1.dropna()
    print(sample_1)

    def get_date(sample_1):
        return math.floor(sample_1['측정일시'] / 100)

    sample_1['측정일시'] = sample_1.apply(get_date, axis=1)
    sample_2 = sample_1['측정일시']
    print(sample_2)

    group1 = sample_1.groupby(['지역', '측정소코드', '측정소명', '측정일시', '주소'], as_index=False)
    group1 = group1.mean()

    def get_date(group1):
        return round(group1['PM10'])
    group1['PM10'] = group1.apply(get_date, axis=1)
    print(group1)
    group1.to_excel(url1[i], sheet_name='Sheet1')
