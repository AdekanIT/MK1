
n = int(input('Enter the num: '))

if n%2==1:
    print('Werid')
elif n%2==0:
    print('Not Werid')
elif n%2==1 and 2 <= n <= 5:
    print('Weird')
elif n%2==0 and 2 <= n <= 5:
    print('Not Weird')
elif  n%2==1 and 6 <= n <= 20:
    print('Weird')
elif n%2==0 and 6 <= n <= 20:
    print('Not Weird')
elif n%2==1 and  n > 20:
    print('Weird')
elif n%2==0 and  n > 20:
    print('Not Weird')