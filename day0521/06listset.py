days_list=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
print()
print(days_list)

days_set = set(days_list)
print(days_set) #순서가 흐트러짐


days_set.add(377) #set추가는 add()
days_set.add(45) #list는 append(), insert(1,2)
print(days_set)
days_set.remove('Wed')
days_set.discard('Mon')
print(days_set)