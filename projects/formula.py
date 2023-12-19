n = int(input('Enter the number: '))
if n < 0:
    print('This is not positive nomber')
elif n > 0:
    sum = ((n)*(n+1))/2
    print(f'This is positive number: {sum}')