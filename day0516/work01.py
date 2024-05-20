#문제 해결

name = ' '
age = 0
fit = 0.0

#문제
#input() 이름,나이,fit 입력받고, 형변환
#예외처리
#print()출력

try:
    name = str(input('name >>> ')) #문자열변환 str()
    age = int(input('age >>> ')) #정수형변환 int()
    fit = float(input('height >>> ')) #실수형변환 float()
except Exception as ex:
    print('데이터 오류입니다 \n', ex)   
