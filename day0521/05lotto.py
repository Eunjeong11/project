#05lotto.py문서 set복합데이터로 난수확인

import random
lotto = set() #set인식 {}표시하면 기본이 dict인식함
result = True

while result:
    num = random.randint(1,45)
    if len(lotto) >=6:
        result = False
    else:
        #리스트lotto.append(num)
        lotto.add(num)


print()
print(lotto)
mylotto = list(lotto)
mylotto.sort()
print(mylotto)
