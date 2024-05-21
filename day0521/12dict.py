mysite = { 1:'naver', 2:'kakao', 3:'python'} 


# 출력1
print(mysite)

# 출력2 for 반복문 일반적인 접근방법
for k in mysite:
    print(k, ':', mysite[k])

print('-'*50)
for i, k in enumerate(mysite):
    # print(i, ' ', k) #i=순서 k=키값
    # print(i, '번째', k, ':', mysite[k])
    print(k, ':', mysite[k])

print()
for k,v in mysite.items():
    print(k, ':', v)




print()