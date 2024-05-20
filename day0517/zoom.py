#import LG #import LG물리적인 파일명
from LG import user_id, user_pwd, note, game
import time
from datetime import datetime

#O'REILLY교재 p.75
# zoom.py에서 LG.py문서 전역변수 및 함수접근
print('-'*100)
print('zoom.py')
print()

time.sleep(1) #Thread.sleep(1000=1초), setTimeout(1, 2000=2초)
print(user_id)
print(user_pwd)
time.sleep(1)
note()
time.sleep(1)
game()
print()

dt = datetime.now()
print(dt)



print('-'*100)
print()