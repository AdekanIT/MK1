text = input('Enter the text: ')
text_base = []

for char in text:
    if char:
        text_base.append(char)

reversed_word = text_base.copy()
reversed_word.reverse()

if text_base == reversed_word:
    print('This is palindrome!')
else:
    print('This is not a palidrom!')