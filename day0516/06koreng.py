
kor=90; eng=85
hap=0; avg=0.0
msg='안내문'
grade='F'

#파이썬 키보드입력 문자값 = input('안내문')
#파이썬 형변환 str(), int(), float()
#순서4 키보드입력 Scanner클래스X, <input type=text name=pay>
kor = input('국어입력 >>> ')
eng = input('영어입력 >>> ')

#순서1 총점, 평균
hap = int(kor)+int(eng)
avg = int(hap/2)
print('kor = ', kor)
print('eng = ', eng)
print('hap = ', hap)
print('avg = ', avg)

#순서2 if~else 평균점수 70점부터 합격, 0~69 재시험
if avg >= 70:
    msg='pass'
else:
    msg='fale'    

#순서3 if~elif~else 평균점수 100~90 A, 89~80 B, 79~70 C, 69~60 D, 59~0 F
if avg >= 90:
    grade='A'
elif avg >= 80:
    grade='B'
elif avg >= 70:
    grade='C'
elif avg >= 60:
    grade='D'
else:
    grade='F'       

print('총점 = ', hap)
print('평균 = ', avg)
print('학점 = ', grade)
print('합격여부 = ', msg)