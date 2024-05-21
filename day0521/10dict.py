mysite = { 1:'naver', 2:'kakao' } #dict
print(mysite)

#해결1 항목추가 3 python 추가 add,append,insert 사용X
mysite[3] = 'python'
print(mysite)

#해결2 1번값을 아마존
mysite[1] = 'amazon'
print(mysite)

#해결3 2번값 카카오만 출력
print(mysite[2]) #[키값]
print(mysite.get(2)) #get()함수로 접근

print()
#해결4 3,5번값 있는지 확인 in
print(5 in mysite) #False
print(3 in mysite) #True




print()