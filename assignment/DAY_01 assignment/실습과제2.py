import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import csv
import platform

weather_df =pd.read_csv('daegu-utf8-df.csv', encoding='utf-8-sig')
weather_df['날짜']=pd.to_datetime(weather_df['날짜'], format='%Y-%m-%d')

weather_df['최고기온'].astype('float')
weather_df['최저기온'].astype('float')

start_year = int(input('시작 연도를 입력하세요 : '))
end_year = int(input('끝 연도를 입력하세요 : '))

cal_month = int(input('기온 변화를 측정할 달을 입력하세요 : '))


max_list =[]
min_list =[]

weather_df['날짜'].dt.year

for y in range(start_year, end_year+1):
    yearDF = weather_df[(weather_df['날짜'].dt.year == y) & (weather_df['날짜'].dt.month == cal_month)]
    max_list.append(round(yearDF['최고기온'].mean(),1))
    min_list.append(round(yearDF['최저기온'].mean(),1))

plt.rcParams['axes.unicode_minus']= False
plt.figure(figsize=(20,4))
plt.plot(range(start_year,end_year+1), max_list, color ='r', label='최고기온 평균', marker='s')
plt.plot(range(start_year,end_year+1), min_list, color = 'b', label='최저기온 평균', marker='s')
plt.xticks(range(start_year,end_year+1))
plt.legend()
plt.title('{}년부터 {}년까지 {}월 기온 변화'.format(start_year, end_year,cal_month))
plt.show()