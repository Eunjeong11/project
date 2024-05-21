#파일처리

path = 'c:/Mtest/aaa.txt'
file = open(path, 'a', encoding='utf-8')
name = input('name>>> ')
age = input('age>>> ')
juso = input('address>>> ')

file.write(name +'\n')
file.write(age +'\n')
file.write(juso +'\n')
file.close() #권장
print(path, 'file save success')

'''
path = 'c:/Mtest/aaa.txt'
wfile = open(path, 'w', encoding='utf-8') #쓰기wirte
wfile = open(path, 'r', encoding='utf-8') #읽기read
wfile = open(path, 'a', encoding='utf-8') #존재하면 뒤쪽에 추가append

with open(path, 'w', encoding='utf-8') as myfile:
    pass
    # myfile.함수()

#오소리 p.126 파일함수 read(), write(1)

#200제 예제 p.226~252

'''
