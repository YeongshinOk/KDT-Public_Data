import csv
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib

def print_population(population):
    '''
    특정 지역의 인구 현황을 화면에 출력함
    :param population:
    :return:
    '''
    for i in range(len(population)):
        print(f'{i:3d}세: {population[i]:4d}명', end=' ')
        if (i + 1) % 10 == 0:
            print()
    print()

def draw_gender_population(title, male_num_list, female_num_list):

    plt.barh(range(len(male_num_list)), male_num_list, align='center', label='남자')
    plt.barh(range(len(female_num_list)), female_num_list, align='center', label='여자')
    plt.rcParams['axes.unicode_minus']= False
    plt.title(title+'성별 인구 비율')
    plt.legend()
    plt.show()

def calculate_population():
    f = open('gender.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    male_num_list = []
    female_num_list = []

    district = input('시군구 이름을 입력하세요: ')
    for row in data:
        if district in row[0]:
            for male in row[106:207]:
                if ',' in male:
                    male = male.replace(',' , '')
                male_num_list.append(-int(male))

            for female in row[209:310]:
                if ',' in female:
                    female = female.replace(',' , '')
                female_num_list.append(int(female))
            break

    f.close()

    print(f'남성 총 인구수:{sum(male_num_list):,}')
    print_population(male_num_list)
    print('-----------------------------------')
    print(f'여성 총 인구수:{sum(female_num_list):,}')
    print_population(female_num_list)
    draw_gender_population(district, male_num_list, female_num_list)

calculate_population()
