#mytestA.py

#p.96 import 접근 모듈접근
import LG
import time

print('mytestA.py LG모듈import\n')
print('계정id ', LG.user_id)
print('계정pw ', LG.user_pwd)
print()

time.sleep(1) #지연시간 1초
LG.note('마카롱', 2700) #매개인자
time.sleep(1)
LG.game() #일반함수