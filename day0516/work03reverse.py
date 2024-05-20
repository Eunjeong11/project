#work03reverse.py
#해결 while반복문 - 연산
su=5972

#print('역순', 2795)

na=0; rev=0
while True:
   na = su%10
   su = su//10
   rev = rev*10+na
   if su == 0:
        break
print('역순', rev)