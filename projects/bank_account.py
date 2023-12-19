class BanckAcount:
    def __init__(self, client, balance=0.0):
        self.client = client
        self.balance = balance

    def deposit(self, deposit):
        self.balance += deposit
        

    def cash(self, cash_money):
        self.balance -= cash_money
        

    def balance_client(self):
        return self.balance

name = input('Enter your name: ')
client1 = BanckAcount(client = name)

while True:
    action = input('Enter the command: ')  
    if action.lower() == 'deposit':
        sum = float(input('Enter the count of money you want to deposit: '))
        client1.deposit(sum)
    elif action.lower() == 'cash':
        sum = float(input('Enter the count of money you want to cash: '))
        if sum <= client1.balance:
            client1.cash(sum)
            print('Action done!')
        else:
            print('You have not enough money to cash it!')       
    elif action.lower() == 'balance':
        print(client1.balance_client())
    else:
        print('WTF?!')
