print()
import time

class MyClass:
    var = '안녕하세요 짱구' #클래스영역에서 전역변수 접근은 this키워드대신 self사용

    def __init__(self, name):
        print('\n생성자')
        print(name, '님 환영합니다')
        print(self.var)

    #p.113 2번라인
    def __del__(self):
        print('MyClass 소멸자')

    def sayHello(self):
        print('sayHello함수')
        print(self.var)

class Child(MyClass):
    def calculator(self,a,b):
        c=a+b
        return c

obj = Child('aa')
ret1 = obj.calculator(2,3); print(ret1)
ret2 = obj.calculator(7,8); print(ret2)

#p.115 클래스상속 다중상속도 가능함
#p.114 class상속 class 자식이름(부모클래스)
