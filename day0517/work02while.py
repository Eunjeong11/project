#for 대표변수 in range(시작, 끝+1, 증분)
#문제해결1 5개씩 출력하세요 while반복문

su = 0
while True:
    su=su+1
    if su%5==1:
        print()
    if su==31:
        break
    print(su, end='\t')

    #1~30숫자출력 5개씩 6줄