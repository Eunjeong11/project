mysite = { 'aa':'naver', 'bb':'kakao', 'cc':'python'} 


# 출력1
print(mysite)

# 출력2 for 반복문 일반적인 접근방법

for k in mysite:
    print(k, ':', mysite[k])

print()
print(mysite.keys())
print(mysite.values())
print(mysite.items())

print()