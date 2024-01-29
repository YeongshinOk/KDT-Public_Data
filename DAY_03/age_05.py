import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

def draw_piechart(city_name, city_population, voting_population):
    '''
    전체 인구수 대비 투표 가능 인구의 파이차트 작성
    :param city_name:
    :param city_population:
    :param voting_population:
    :return:
    '''

    non_voting_population = city_population - voting_population
    population = [non_voting_population, voting_population]

    color = ['tomato', 'royalblue']
    plt.pie(population, labels=['18세 미만', '투표가능인구'],
            autopct='%.1f%%', startangle=90, colors=color)

    plt.legend(loc=1)
    plt.title(city_name + '투표 가능 인구 비율')
    plt.show()

def get_voting_population(city):
    '''
    투표 가능 인구수 분석 row[21:]
    전체 인구수 : row[1]
    :param city:
    :return:
    '''
    f = open('age.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    header = next(data)

    voting_number_list = []
    city_name = ''
    city_population = 0
    voting_population = 0
    for row in data:
        if city in row[0]:
            city_population = row[1]
            if ',' in city_population:
                city_population = city_population.replace(',', '')
            city_population = int(city_population)
            city_name = row[0]
            for data in row[21:]:
                if ',' in data:
                    data = data.replace(',', '')
                voting_num = int(data)

                voting_number_list.append(voting_num)

                voting_population+= voting_num
            break

    f.close()
    print(f'{city_name}전체 인구수: {city_population:,}명,'
          f'투표 가능 인구수: {voting_population:,}명')

    draw_piechart(city_name, city_population, voting_population)

city = input('투표 가능 인구수를 확인할 도시이름을 입력하시오: ')
get_voting_population(city)