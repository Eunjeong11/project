#파이썬 define 타입x 함수이름(매개인자): 라인개행 후 내용기술 return값
#복하합데이터 액면 그대로 출력
def mydata():
    listdata=['blue', 23, 'F', 78.9, True, 'Monday']
    print(listdata)

    tupledata=(27.45268, 136.4872, 78)
    print(tupledata)

    setdata= {'ab', 'blue', 'ab', 12, 'ab', 12} #순서x, 중복x
    print(setdata)

    dictdata= { 1:'bc', 2:'kb'}
    print(dictdata)

print('함수연습 testing')
#파이썬 함수를 호출하면 기본적으로 main연결되어있음
if __name__ == '__main__':
    mydata()


mydata()
print()