class BankAccount:

    def __init__(self, int_rate = .22, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee to your account.")
            self.balance -= 5.00
        return self

    def display_account_info(self):
        print("Account intrest rate:", self.int_rate)
        print("Balance:", self.balance)

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        else:
            print("Insufficient balance: Intrest could not apply")
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    # other methods
    
    def make_deposit(self, amount):
    # your code here
        self.account.deposit(amount)
        return self
    
    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self


sonnychhuon12345 = User("Sonny", "sonnyc@gmail.com")
sonnychhuon12345.make_deposit(3600).make_deposit(600).make_withdraw(1250+2950)

sonnychhuon12345.display_user_balance()








