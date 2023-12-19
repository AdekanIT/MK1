import random
player1 = input('Выберите: камень, ножницы или бумага: ')
player2 = random.choice(['камень', 'ножницы', 'бумага'])
print(f'Игрок2 выбрал {player2}')

if player1 == 'камень' and player2 == 'ножницы':
    print('Вы выграли!')
elif player1 == 'камень' and player2 == 'бумага':
    print('Вы проиграли!')
elif player1 == 'камень' and player2 == 'камень':
    print('Ничя!')
elif player1 == 'ножницы' and player2 == 'камень':
    print('Вы проиграли!')
elif player1 == 'ножницы' and player2 == 'бумага':
    print('Вы выграли!')
elif player1 == 'ножницы' and player2 == 'ножницы':
    print('Ничья!')
elif player1 == 'бумага' and player2 == 'камень':
    print('Вы выграли!')
elif player1 == 'бумага' and player2 == 'ножницы':
    print('Вы проиграли!')
elif player1 == 'бумага' and player2 == 'бумага':
    print('Ничя!')
else:
    print('WTF?')

