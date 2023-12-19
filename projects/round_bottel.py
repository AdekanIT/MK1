a = int(input('How many bottels: '))
b = float(input('How much litters bottels: '))
c = 0.10
d = 0.25


if b == 1:
    bot=a*c
    print((f'{a} x 0.10$={round(bot, 2)}$'))
elif b == 1.5:
    bot1=a*d
    print((f'{a} x 0.25$ = {round(bot1, 2)}$'))
else:
    print('WTF!')