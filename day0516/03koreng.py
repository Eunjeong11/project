
kor=90
eng=85
hap=0
avg=0.0
msg='안내문'
grade='F'

#순서1 총점, 평균

hap = kor+eng
avg = hap/2
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