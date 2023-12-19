names = []
numbers = []
services = []

while True:
    action = input('Enter the action: ')
    if action.title() == 'Add Name':
        name = input('Enter the new name: ')
        if name in names:
            print('This name exist!')
        else:
            names.append(name)
            print(names)
            print(numbers)
            print(services)
            print('Action done!')
    elif action.title() == 'Remove Name':
        name_remove = input('Enter the name which u wanna remove: ')
        if name_remove.title() in names:
            print('This name not exist!')
        else:
            names.remove(f'{name_remove}')
            print(names)
            print(numbers)
            print(services)
            print('Action done!')
    elif action.title() == 'Change Name':
        name_change = input('Enter the name which u wanna change: ')
        if name_change.title() not in names:
            print('This name is not exist!')
        else:
            name_add = input('Enter tha name which u wanna add for new changed name: ')
            name_index = names.index(name_change)
            names.pop(name_index)
            names.append(name_add)
            print(names)
            print(numbers)
            print(services)
            print('Action done!')
    elif action.title() == 'Add Number':
        number = input('Enter the new number: ')
        if number.title() in numbers:
            print('This number exist!')
        else:
            numbers.append(number)
            print(names)
            print(numbers)
            print(services)
            print('Action done!')
    elif action.title() == 'Remove Number':
        number_remove = input('Enter the number which u wanna remove: ')
        if number_remove.title() not in names:
            print('This number is not exist!')
        else:
            numbers.remove(f'{number_remove}')
            print(names)
            print(numbers)
            print(services)
            print('Action done!')
    elif action.title() == 'Change Number':
        number_change = input('Enter the number which u wanna change: ')
        if number_change.title() not in numbers:
            print('This name is not exist!')
        else:
            number_add = input('Enter tha number which u wanna add for new changed name: ')
            number_index = numbers.index(number_change)
            numbers.pop(number_index)
            numbers.append(number_add)
            print(names)
            print(numbers)
            print(services)
            print('Action done!')
    elif action.title() == 'Add Service':
        service = input('Enter the new service: ')
        if service in services:
            print('This service exist!')
        else:
            services.append(f'{service}')
            print(names)
            print(numbers)
            print(services)
            print('Action done!')
    elif action.title() == 'Remove Service':
        service_remove = input('Enter the service which u wanna remove: ')
        if service_remove.title() not in services:
            print('This number is not exist!')
        else:
            services.remove(f'{service_remove}')
            print(names)
            print(numbers)
            print(services)
            print('Action done!')
    elif action.title() == 'Change Service':
        service_change = input('Enter the service which u wanna change: ')
        if service_change.title() not in services:
            print('This service is not exist!')
        else:
            service_add = input('Enter tha service which u wanna add for new changed name: ')
            service_index = services.index(service_change)
            services.pop(service_index)
            services.append(service_add)
            print(names)
            print(numbers)
            print(services)
            print('Action done!')
    else:
        print('WTF?!')


