dan = 17

#문제1 for 반복문
print('for반복문\n')
for i in range(1, 10):
    # print(dan, '*', i, '=', dan*i)
    # print('{} * {} = {}'.format(dan,i,(dan*i)))
    print(f'{dan} * {i} = {(dan*i)}')

#문제2 while 반복문
print('\nwhile반복문')
j=1
while True:
    print(dan, '*', j, '=', dan*j)
    j=j+1
    if j == 10:
        break
print()