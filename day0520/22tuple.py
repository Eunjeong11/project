#오소리 p.86

pos = ('시청', 36.73982, 127.92851) #튜플 변경불가, 추가, 수정 XXXXX
print(pos) 
x,y,z = pos
print(x)
print(y)
print(z)
print()

my = list(pos) #int(), str(), float(), list(), tuple()
print(my) #list
my.append('홍대')
print(my) #리스트
pos = tuple(my)
print(pos)


#에러 pos.append('홍대') 튜플은 append()안됨
#에러 pos.insert(2,'합정') insert도 안됨
print(pos)
print()