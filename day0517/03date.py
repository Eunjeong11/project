#02date.py
#O'REILLY교재 p.75
#import datetime dt = datetime.datetime.now()
from datetime import datetime #dt = datetime.now()
import time

dt = datetime.now()
print(dt) #2024-05-17 12:24:15.872577
ob = time.localtime() 
print(ob) #time.struct_time(tm_year=2024~


#배열array 용어보다는 리스트 list 명명함, 파이썬 리스트는 혼합형
lotto = [7, 19, 23, 26, 31, 45] #int정수형구성 리스트
mydata = ['kim', 90, 85, 87.5, True, 'B', '합격'] #혼합리스트
week = ['mon', 'tue', 'wed', 'thr', 'fri', 'sat', 'sun'] #문자열구성 리스트

my = ob.tm_wday #숫자출력
print('요일출력', my) #숫자출력
print(week[my]) #week출력 0,1,2,3,4,5,6
if my==0:
    print('Today`s monday')
elif my==1:
    print('Today`s tuesday')
elif my==2:
    print('Today`s wendsday')
elif my==3:
    print('Today`s thursday')
elif my==4:
    print('Today`s friday')
elif my==5:
    print('Today`s saturday')
else:
    print('Today`s sunday')

#p.76
