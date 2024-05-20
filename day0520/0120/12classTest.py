print()
import time

class MyClass:
    var = '안녕하세요' #클래스영역에서 전역변수 접근은 this키워드대신 self사용
    def sayHello(self):
        print('sayHello함수')
        print(self.var)

obj = MyClass() #MyClass 인스턴스 객체 생성
print(obj.var)
print()

time.sleep(1)
obj.sayHello()

#p.106 class = 전역변수 + 생성자 + 일반함수
