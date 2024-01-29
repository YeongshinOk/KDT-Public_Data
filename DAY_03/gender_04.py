import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib
import platform


f= open('gender.csv', encoding='utf-8-sig')
data = csv.reader(f)
city_list = ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시','울산광역시']

for city in city_list:
    male_list = []
    female_list = []
    for row in data:
        if city in row[0]:
            for i in range(106, 207):
                male_list.append(int(row[i].replace(',', '')))
                female_list.append(int(row[i+103].replace(',', '')))
            break

    color = ['cornflowerblue', 'tomato']
    plt.plot(male_list, color=color[0], label='남성')
    plt.plot(female_list, color=color[1], label='여성')
    plt.title(city + '남녀 인구수 비교')
    plt.xlabel('나이')
    plt.ylabel('인구수')
    plt.legend()
    plt.savefig('img/' + city + '.png', dpi=100)
    plt.close()