#p.73 문자열슬라이싱

data = 'Time is money!!'
print(data[1:5])
print(data[:7])
print(data[9:])
print(data[:-3])
print()

#p.77
data = 'I love python'
listdata = ['a','b','c', data]
#print(listdata)
print(data) #I love python
print(list(data)) #['I', ' ', 'l', 'o', 'v', 'e', ' ', 'p', 'y', 't', 'h', 'o', 'n']
print()

for i in range(len(data)): #비권장
    print(data[i], end='')
print()