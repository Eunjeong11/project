print()


#18list.py
dt=[5,7,33]
print(dt)

dt.append(9)
print(dt)

dt.insert(1, 46) #[5, 46, 7, 33, 9] insert(위치, 데이터)
print(dt)
print('-' * 100)

ret1 = dt.index(7)
print('dt.index(7)위치 ' , ret1, '번째')

#ret2 = dt.index(23) #23데이터가없으면 에러발생
#print('dt.index(23)위치 ' , ret2, '번째')

dt.remove(33)
print(dt)

#dt.remove(2 위치가 아니라 값으로 삭제) 2데이터가없으면 에러발생

dt.append(71)
dt.append(24)
dt.append(3)
dt.append(15)
print(dt) #[5, 46, 7, 9, 71, 24, 3, 15]

#해결1 46 7 9 추출슬라이싱 [시작:끝+1]
print(dt[1:4])

#해결2 46 7 9 삭제 remove, del 리스트[], [시작:끝+1]
#del dt[1:4]
#dt[1:4]=[]
del dt[3:] #한건 데이터값으로 삭제는 remove()
print(dt)
print()

#리스트 함수 append, insert, remove, del키워드, index, sort
#리스트.remove(값
#del 리스트[위치]
#del 리스트[시작:끝+1]

myhobby=['game',"python", 78.9, 'F', 21, True]
#해결3 for 반복문 출력
print(myhobby)
for i in range(len(myhobby)):
   #비추천 print('[',i,'] =',myhobby[i])
   print(myhobby[i], end=' ')

#해결4 sort(), reverse()
print()
su = [5,46,7,9,71,24,3,15]
print(su)
su.sort()
print(su)
su.reverse()
print(su)
#리스트는 최대장점 순서가 있고, 중복허용, 많은 함수가 제공
#리스트는 맨마지막에 추가 append(), 맨마지막부터 pop()
#리스트는 데이터 한번에 삭제 clear()


print()
