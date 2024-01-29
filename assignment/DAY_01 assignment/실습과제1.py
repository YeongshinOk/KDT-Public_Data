import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import csv
import platform

weather_df =pd.read_csv('daegu-utf8-df.csv', encoding='utf-8-sig')
weather_df['날짜']=pd.to_datetime(weather_df['날짜'], format='%Y-%m-%d')

weather_df['최고기온'].astype('float')
weather_df['최저기온'].astype('float')


weather_df['일교차']=weather_df['최고기온']-weather_df['최저기온']

tem_ran_max_list = []

for y in range(2014, 2024):
    high_max = -999
    month_max = 0
    yearDF = weather_df[weather_df['날짜'].dt.year == y]

    for m in range(1, 13):
        ymDF = yearDF[yearDF['날짜'].dt.month == m]
        tem_ran = ymDF['일교차'].mean()
        if tem_ran > high_max:
            high_max = tem_ran
            month_max = m
    tem_ran_max_list.append([y,month_max,round(high_max,1)])

print(tem_ran_max_list)

plt.figure(figsize=(10,6))
plt.bar([i[0] for i in tem_ran_max_list],[i[2] for i in tem_ran_max_list], color='skyblue')
plt.xticks([i[0] for i in tem_ran_max_list],[f'{i[0]}.{i[1]}' for i in tem_ran_max_list])
plt.xlabel('Year/Month')
plt.ylabel('일교차')
plt.title('지난 10년간 대구의 일교차가 가장 큰 달')

plt.show()