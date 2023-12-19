names = ['Igor', 'Pavel', 'Jordan', 'Loki',
        'apsent', 'up','down', 
        'ASDES', 'JOONY', 'LIL', 'LOL']
func_list = [i + '2' for i in names]
step = [add + '!' for add in names if 'a' in add] 
end = [end + '?' for end in names]
low = [low for low in names if low.islower()]
uppers = [upper for upper in names if upper.isupper()]
chotni = [x for x in range(1,11) if x%2 != 1]
odd = [x for x in range(1,11) if x%2 != 0]
squer = [x**2 for x in range(1,11)]



print(func_list)
print(step)
print(end[0::2])
print(low)
print(uppers)
print(chotni)
print(odd)
print(squer)