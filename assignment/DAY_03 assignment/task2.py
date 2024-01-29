key = 1
while key == 1:
    n = input('홀수차 배열의 크기를 입력하세요: ')
    if not n.isdecimal():
        print('문자를 입력하였습니다. 홀수의 숫자를 입력하세요.')
        continue
    else:
        key = 2
        n=int(n)
        while key == 2:
            if n % 2 == 0:
                print('짝수를 입력하였습니다. 다시 입력하세요.')
                key = 1
                continue
            break

square = [[0 for col in range(n)] for row in range(n)]

x = n // 2
y = 0

for i in range(n**2):
    square[y][x] = i + 1
    x1 = (x+1) % n
    y1 = (y-1) % n
    if square[y1][x1] != 0:
        y += 1
    else:
        x = x1
        y = y1

print(f'Magic Square ({n}x{n})')
for i in square:
    for j in i:
        print(f'{j:10}', end=' ')
    print()