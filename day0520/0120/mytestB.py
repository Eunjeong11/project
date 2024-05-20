#mytestB.py
#p.96 from ~ import접근

#import LG
from LG import user_id, user_pwd, note,  game
from time import sleep

print('mytestB.py LG모듈 from ~ import\n')
print('계정id ', user_id)
print('계정pw ', user_pwd)
print()

sleep(1) #지연시간 1초
note('김치찌개', 2700) #매개인자
sleep(1)
game() #일반함수