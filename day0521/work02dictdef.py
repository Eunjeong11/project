import random
import time
import math
import sys #프로그램종료 sys.exit()

menu = { } #메뉴이름을 key, 메뉴가격을 value
bl = True
num = 0

def saveMenu():
    name=input('key메뉴이름>>>')
    price=int(input('value가격입력>>> '))
    menu[name]=price
    print(name+'키값 등록 성공')

def selectAllMenu():
    for k in menu:
        print(k, ':', menu[k])

def editMenu():
    name=input('수정할메뉴>>> ')
    if menu.get(name) == None:
        print(name, '은(는) 없는 메뉴입니다')
    else:
        price=int(input('수정가격입력>>> '))
        menu[name]=price
        print(name+'수정 완료되었습니다')

def deleteMenu():
    name=input('삭제할메뉴>>> ')
    if menu.get(name) != None:
        del menu[name]
        print(name, '삭제 완료되었습니다')
    else:
        print(name, '은(는) 없는 메뉴입니다')  

def searchMenu():
    name=input('메뉴입력>>> ')
    if menu.get(name) != None:
        print(name, '의 가격은', menu[name], '입니다')
    else:
        print(name, '은(는) 없는 메뉴입니다')

def exitMenu():
    print('program exit')
    sys.exit()

if __name__=='__main__':
    while bl:
        print()
        print('1.추가 2.출력 3.수정 4.삭제 5.조회 9.종료')
        num = int(input('>>> '))
        if num==9:
            print('프로그램을 종료합니다')
            bl=False
            sys.exit()
        elif num==1: #항목추가 add,append,insert 사용불가
            saveMenu()

        elif num==2: #전체출력 고전적인방법 for k in menu
            selectAllMenu()

        elif num==3: #메뉴key수정, 수정할때 get() 결과none일때 수정못함
            editMenu()
            
        elif num==4: #메뉴key삭제, 삭제할때 get() 결과none일때 삭제못함
            deleteMenu()

        elif num==5: #메뉴key조회 결과none일때 검색못함
            searchMenu()

        else:
            exitMenu()
    


