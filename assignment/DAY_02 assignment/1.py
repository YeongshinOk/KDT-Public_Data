# 지하철 각 노선별 최대 하차 인원을 막대그래프로 표시하고, 하차인원 출력
import csv

import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

df = pd.read_csv('subwaytime.csv',encoding='utf-8-sig',sheet_name='지하철 시간대별 이용현황', header=[0,1])
df.head()
