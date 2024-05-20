#mytestC.py
#p.96 from ~ import접근

#import LG
import LG as my
import time

print('mytestB.py LG모듈 from ~ import\n')
print('계정id ', my.user_id)
print('계정pw ', my.user_pwd)
print()

time.sleep(1) #지연시간 1초
my.note('마카롱김치찌개', 2700) #매개인자
time.sleep(1)
my.game() #일반함수