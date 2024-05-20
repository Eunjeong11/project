print()
import time

class MyClass:
    var = '안녕하세요 짱구' #클래스영역에서 전역변수 접근은 this키워드대신 self사용

    def __init__(self, name):
        print('\n생성자')
        print(name, '님 환영합니다')
        print(self.var)

    def sayHello(self):
        print('sayHello함수')
        print(self.var)

obj = MyClass('kim') #MyClass 인스턴스 객체 생성
print(obj.var)
print()

time.sleep(1)
obj.sayHello()

#p.111 class = 전역변수 + 생성자 + 일반함수
