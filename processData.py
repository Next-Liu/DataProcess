import pandas as pd
import os

folderList = ['../data/20200101-20201231', '../data/20210101-20211231', '../data/20220101-20221231',
               '../data/20230101-20231231']
#folderPath = '../data/20200101-20201231'
folderPath = '../data/test'
df = pd.read_csv('../data/20200101-20201231/china_sites_20200101.csv')

final_data = []

# 遍历df
for fileName in os.listdir(folderPath):
    df = pd.read_csv(folderPath + '/' + fileName)
    temp_hour = 0
    count = 0
    temp_data = []
    print(fileName)
    for i in range(len(df)):
        date = df.iloc[i]['date']
        hour = df.iloc[i]['hour']
        if hour == 0 and count == 0:
            temp_data = [date, hour]
        if hour == temp_hour:
            count += 1
            if df.iloc[i]['type'] == 'AQI':
                temp_data.append(df.iloc[i]['1036A'])
            if df.iloc[i]['type'] == 'PM2.5':
                value = df.iloc[i]['1036A']
                temp_data.append(value if value != '' else 0)
            if df.iloc[i]['type'] == 'PM10':
                value = df.iloc[i]['1036A']
                temp_data.append(value if value != '' else 0)
            if df.iloc[i]['type'] == 'SO2':
                value = df.iloc[i]['1036A']
                temp_data.append(value if value != '' else 0)
            if df.iloc[i]['type'] == 'NO2':
                value = df.iloc[i]['1036A']
                temp_data.append(value if value != '' else 0)
            if df.iloc[i]['type'] == 'O3':
                value = df.iloc[i]['1036A']
                temp_data.append(value if value != '' else 0)
            if df.iloc[i]['type'] == 'CO':
                value = df.iloc[i]['1036A']
                temp_data.append(value if value != '' else 0)
        if hour != temp_hour:
            final_data.append(temp_data)
            temp_hour += 1
            temp_data = [date, temp_hour]
            if df.iloc[i]['type'] == 'AQI':
                temp_data.append(df.iloc[i]['1036A'])
        if i == len(df) - 1:
            final_data.append(temp_data)

columns = ['date', 'hour', 'AQI', 'PM2.5', 'PM10', 'SO2', 'NO2', 'O3', 'CO']
# 将final_data的元素依次添加到dataframe中
new_df = pd.DataFrame(columns=columns)
for i in range(len(final_data)):
    new_df = new_df.append(pd.DataFrame([final_data[i]], columns=columns))
new_df.to_csv('1036A_2020.csv', index=False)
