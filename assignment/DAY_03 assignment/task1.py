import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib
import platform



def draw_pie_chart(region, population):
    color = ['cornflowerblue', 'tomato']
    plt.pie(population, labels=['남성', '여성'], colors=color, startangle=90, autopct='%.1f%%')
    plt.title(region, fontsize=10)
    # plt.show()


def subplots(region_list, population_list):
    plt.figure(figsize=(10, 10), dpi=200)
    fig, axe = plt.subplots(nrows=3, ncols=3)

    row = 0
    for i in range(len(region_list)):
        plt.axes(axe[row][i%3])
        draw_pie_chart(region_list[i], population_list[i])
        if i % 3 ==2 : row += 1
        # plt.show()

    fig.suptitle('대구광역시 구별 남녀 인구 비율',fontsize=20)
    plt.tight_layout()
    plt.show()


f= open('gender.csv', encoding='utf-8-sig')
data = csv.reader(f)

region_list = ('대구광역시','대구광역시 중구', '대구광역시 동구', '대구광역시 서구','대구광역시 남구',
                 '대구광역시 북구','대구광역시 수성구', '대구광역시 달서구', '대구광역시 달성군')
population_list = []

for row in data:
    for region in region_list:
        if region in row[0]:
            male_count = int(row[104].replace(',', ''))
            female_count = int(row[207].replace(',', ''))
            population_list.append([male_count, female_count])
            print(population_list)
            # male_count = 0
            # female_count = 0
            break

subplots(region_list, population_list)

