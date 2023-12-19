class User:
    def __init__(self, username, email, age, phone):
        self.username = username
        self.email = email
        self.age = age
        self.phone = phone

    def change_username(self, new_username):
        self.username = new_username
    
    def change_email(self, new_email):
        self.email = new_email

    def change_phone(self, new_phone):
        self.phone = new_phone

   
username1 = input('Enter your username: '),
email1 = input('Enter your email: '),
age1 = int(input('Enter your age: ')),
phone1 = int(input('Enter your phone number: '))
user = User(username=username1,
            email=email1,
            age=age1,
            phone=phone1)


while True:
    action = input('Enter the command: ')
    if action.lower() == 'change username':
        new_username = input('Enter the new username: ')
        user.change_username(new_username = new_username)
        print(user.username)
    elif action.lower() == 'change email':
        new_email = input('Enter the new email: ')
        user.change_email(new_email = new_email)
        print(user.email)
    elif action.lower() == 'change phone':
        new_phone = int(input('Enter the new phone number: '))
        user.change_phone(new_phone = new_phone)
        print(user.phone)
    else:
        print('WTF?!')
