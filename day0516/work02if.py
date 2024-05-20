#문제 해결

# int a=99, b=11, c=100;//적은숫자 출력
# 		if~else
# 		if(a>b && b>c) {System.out.println(c+" "+b+" "+a);}
# 		else if(b>c && c>a) {System.out.println(a+" "+c+" "+b);}
# 		else if(c>b && b>a) {System.out.println(a+" "+b+" "+c);}
# 		else if(a>c && c>b) {System.out.println(b+" "+c+" "+a);}
# 		else if(b>a && a>c) {System.out.println(c+" "+a+" "+b);}
# 		else {System.out.println(b+" "+a+" "+c);}

a=45; b=11; c=100
if a>b & b>c :
    print(c, b, a)
elif b>c & c>a :
    print(a, c, b)
elif c>b & b>a :
    print(a, b, c)
elif a>c & c>b :
    print(b, c, a)
elif b>a & a>c :
    print(c, a, b)
else:
    print(b, a, c)


print()
x=45; y=100; z=12
su=[150,5,12]

if su[0]>su[1] & su[1]>su[2] :
    print(su[2], su[1], su[0])
elif su[1]>su[2] & su[2]>su[0] :
    print(su[0], su[2], su[1])
elif su[2]>su[1] & su[1]>su[0] :
    print(su[0], su[1], su[2])
elif su[0]>su[2] & su[2]>su[1] :
    print(su[1], su[2], su[0])
elif su[1]>su[0] & su[0]>su[2] :
    print(su[2], su[0], su[1])
else:
    print(su[1], su[0], su[2])

print('배열리스트', su[0])
print('배열리스트', su[1])
print('배열리스트', su[2])
