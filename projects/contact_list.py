contact_list=[
    'Post Malon ',
    'Erik ',
    'Pavel',
    'Jordan'
]
print(contact_list)
text = input('Enter the number and name of contact here! :> ')
action = input('Enter the command here! :> ')


if action == 'add':
    contact_list.append(f'{text}')
    contact_list.sort()
    print(contact_list)
elif action == 'remove':
    contact_list.remove(f'{text}')
    contact_list.sort()
    print(contact_list)
elif action == 'change':
    iftext = input('Enter the name of contact you wanne change! :> ')
    text_index = contact_list.index(f'{iftext}')
    contact_list.pop(text_index)
    contact_list.append(f'{text}')
    contact_list.sort()
    print(contact_list)
# elif action == 'change Erik':
#     contact_list.pop(1)
#     contact_list.append(f'{text}')
#     print(contact_list)
# elif action == 'change Pavel':
#     contact_list.pop(2)
#     contact_list.append(f'{text}')
#     print(contact_list)
# elif action == 'change Jordan':
#     contact_list.pop(3)
#     contact_list.append(f'{text}')
#     print(contact_list)
else:
    print('Rewrite command again!')    

