
#for 대표변수 in range(시작, 끝+1, 증분)
hap = 0
su = 0
for a in range(1,10,1):
    su = su + 1
    print(su, end = '\t')
    hap = hap + su

print()
print('hap = ' + hap)

tot = 0
for i in range(1,10,1):
    print(i, end = '\t')
    tot = tot + i

print('tot = ', tot)
print('-'*50)