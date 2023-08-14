class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password


# Task 1
""" Driver Code For Task 1 """

user1 = User('Bob', 1234, 'password')
print('Name: ', user1.name)
print('PIN: ', user1.pin)
print('Password: ', user1.password)

# End of Task 1

# Task 2: Add User Class Instance Methhods


class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, new_name):
        self.name = new_name

    def change_pin(self, new_pin):
        self.pin = new_pin

    def change_password(self, new_password):
        self.password = new_password


""" Driver Code for Task 2 """
bob = User('Bob', 1234, 'pass')
print('Name: ', bob.name)
print('PIN: ', bob.pin)
print('Password: ', bob.password)

bob.change_name('Alice')
bob.change_pin('4567')
bob.change_password('word')

print('New Changes')
print('Name: ', bob.name)
print('PIN: ', bob.pin)
print('Password: ', bob.password)

# Task 3:Create BankUser subclass


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print('Balance is: $', self.balance)

    def withdraw(self, money):
        if self.balance >= money:
            self.balance -= money
        else:
            print('Sorry there is no money here!')

    def deposit(self, money):
        self.balance += money

# Task 5:Transfer and request money
# Added Bonus Task 2 update made to transfer_money() and request_money()

    def transfer_money(self, amount, user):
        pin = int(input('Enter your PIN'))
        if pin == self.pin and self.balance >= amount:
            user.deposit(amount)
            self.withdraw(amount)
            return True
        elif self.balance < amount:
            print('Not enough money to transfer here!')
        else:
            print('Invalid amount:Please enter a positive number')
            return False

    def request_money(self, amount, user):
        if amount > 0:
            pin = int(input('Enter PIN for' + user.name + ': '))
            password = input("Enter password for:" + self.name + ': ')

        if pin == user.pin and password == self.password and user.balance >= amount:
            user.withdraw(amount)
            self.deposit(amount)
            return True
        elif user.balance < amount:
            print('Not enough money to complete the request')
        else:
            print('Invalid amout:Please enter a positive number')
            return False


""" Driver Code for Task 3 """
bank_user = BankUser('Batman', 7895, 'gotham')
print('Name :', bank_user.name)
print('PIN :', bank_user.pin)
print('Password :', bank_user.password)
print('Balance is:$', bank_user.balance)

""" Driver Code for Task 4"""
bank_user2 = BankUser("Superman", 4444, "krptonite")
bank_user2.show_balance()
bank_user2.deposit(1000)
bank_user2.show_balance()
bank_user2.withdraw(500)
bank_user2.show_balance()

print('Name :', bank_user2.name)
print('PIN :', bank_user2.pin)
print('Password :', bank_user2.password)
print('Balance is $', bank_user2.balance)
