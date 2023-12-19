a = int(input('Cost of offer: '))
c = float(a / 100)*12
d = float(a / 100)*18
e = float(a - (c + d))

print(f'Taxes: {round(c, 2)}$')
print(f'Waiters procent: {round(d, 2)}$')
print(f'Clear payment: {round(e, 2)}$')