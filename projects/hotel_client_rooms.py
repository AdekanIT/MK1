clients = {}
rooms = [i for i in range(1, 41)]
booked_room = []

def add_client(client_name, client_room):
    clients[client_name] = client_room
    rooms.remove(client_room)
    booked_room.append(client_room)

def remove(client_name):
    booked_room.remove(clients[client_name])
    rooms.append(clients[client_name])
    clients.pop(client_name)

def show_rooms():
    return booked_room

while True:
    action = input('Enter the command: ')
    if action.upper() == 'REGIST CLIENT':
        client_name = input('Enter client name: ')
        print(rooms)
        client_room = int(input('Enter the client room: '))
        if client_room in rooms:
            add_client(client_name, client_room)
            print(clients)
        else:
            print('This room already booked!')
    elif action.upper() == 'REMOVE CLIENT':
        remove_name = input('Enter the name which you wanna remove: ')
        if remove_name in clients.keys():
            remove(remove_name)
            print('Action done!')
        else:
            print('This client not exist!')
    elif action.upper() == 'SHOW ROOMS':
        print(show_rooms())
    else:
        print('WTF?!')