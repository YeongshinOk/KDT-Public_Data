import csv

f = open('daegu.csv', 'r', encoding='utf-8-sig')
data = csv.reader(f, delimiter=',')
print(data)
count=0
for row in data:
    if count > 5:
        break
    else:
        print(row)
    count+=1

f.close()

# encoding='utf-8-sig'로 '\ufeff' 제거
fin = open('daegu.csv', 'r', encoding='utf-8-sig')
data = csv.reader(fin, delimiter=',')

# newline='' : 한 라인씩 건너 뛰며 저장되는 현상 없앰
fout = open('daegu-utf8.csv', 'w', newline='', encoding='utf-8-sig')
wr = csv.writer(fout)

for row in data:
    for i in range(len(row)):
        row[i]= row[i].replace('\t','')
    print(row)
    wr.writerow(row) # writerow(): 한 행씩 파일로 저장

fin.close()
fout.close()
print('파일 저장 완료')

f = open('daegu-utf8.csv', encoding='utf-8-sig')
data = csv.reader(f, delimiter=',')
header = next(data)
print(header)

i=1
for row in data:
    print(row)
    if i >=5:
        break
    i += 1
f.close()
