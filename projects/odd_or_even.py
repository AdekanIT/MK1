def odd_or_even(a):
    while True:
        if a % 2 == 0:
            print('Even')
        elif a % 2 == 1:
            print('Odd')


odd_or_even(a = int(input('Enter the number: ')))