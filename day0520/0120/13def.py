print()
import time

#class 생략하고 전역변수만, 함수만
var = '안녕쌉싸리와요 명수' #클래스영역에서 전역변수 접근은 this키워드대신 self사용
def sayHello(self):
    print('일반함수sayHello')
    print(self.var)

print(var)
print()

time.sleep(1)
sayHello()

#p.106 class = 전역변수 + 생성자 + 일반함수


print('13def.py 클래스X')