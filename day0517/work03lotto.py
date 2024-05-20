#work03lotto.py
import random

lotto = [] 
num = random.randint(1,10)
#6회발생 for 반복문
for i in range(6):
    while num in lotto: 
        num = random.randint(1,10)#1~45
    lotto.append(num)


print(lotto)
lotto.sort()
print(lotto)
print()
