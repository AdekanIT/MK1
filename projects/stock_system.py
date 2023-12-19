stock = {'In stock': {}}
basket = []

while True:
    action = input('Enter command: ')
    if action.lower() == 'add stock':
        product = input('Enter the product: ')
        if product in stock['In stock'].keys():
            print('This product is already exist!')
        count = int(input('Enter the coun of product: '))
        stock['In stock'][product] = count
        print(stock)
    elif action.lower() == 'clear stock':
        print(stock['In stock'].clear())
    elif action.lower() == 'change stock':
        product = input('Enter the product which you wanna chage: ')
        if product not in stock['In stock'].keys():
            print('This product not exist!')
        else:
            stock['In stock'].pop(product)
            product = input('Enter the product which you wanna add: ')
            count = int(input('Enter the count of product: '))
            stock['In stock'][product] = [count]
            print(stock)
    elif action.lower() == 'remove stock':
        product = input('Enter the product which you wanna remove: ')
        if product not in stock['In stock'].keys():
            print('This product not exist!')
        else:
            stock['In stock'].pop(product)
            print(stock)
    elif action.lower() == 'add basket':
        product = input('Enter the product which you wanna buy: ')
        if product in stock['In stock'].keys():
            count = int(input('Enter how many you wanna buy: '))
            if count > stock['In stock'][product]:
                print('This is more than in stock!')
            else:
                basket.append((product, count))
                stock['In stock'][product] -= count
                print(basket)
        else:
            print('This product does not exist!')