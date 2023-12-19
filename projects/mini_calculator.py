a = int(input('a= '))
b = int(input('b= '))
c = input('Signature = ')

if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/':
    print(a / b)
elif c == '**':
    print(a**b)
elif c == '//':
    print(a//b)
elif c == '%':
    print(a % b)
else:
    print('WTF?')
