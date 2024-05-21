#오소리 p.98
words = ['apple', 'bat', 'bar', 'atom', 'book', 'aws', 'blue', 'cool']
by_letter = {}

for word in words:
    letter = word[0] #첫번째 글자
    if letter not in by_letter:
        by_letter[letter] = [word] #value값 리스트화
    else:
        by_letter[letter].append(word)
print(by_letter)

# for word in words:
#     letter = word[0]
#     by_letter.setdefault(letter, []).append(word)
# print(by_letter)