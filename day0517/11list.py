#10list.py

#리스트는 시작첨자 0번째부터 시작
week = ['mon', 'tue', 'sat', 'sun'] #문자열구성 리스트
print(week)
week.append('추석날')
week.append('토요일')
print(week)
week.insert(1,'삼일절')
print(week)
print()

week.remove('tue')
print(week)