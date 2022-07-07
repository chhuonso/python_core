class BankAccount:
    all_accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate = .22, balance = 0): 
        # your code here! (remember, instance attributes go here)
        self.int_rate = int_rate
        self.balance = balance
        # don't worry about user info here; we'll involve the User class soon
        BankAccount.all_accounts.append(self)
    def deposit(self, amount):
        # your code here
        #  increases the account balance by the given amount
        self.balance += amount
        return self
    def withdraw(self, amount):
        # your code here 
        # decreases the account balance by the given amount if there are sufficient funds;
        #  if there is not enough money, print a message
        #  "Insufficient funds: Charging a $5 fee" and deduct $5
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee to your account.")
            self.balance -= 5.00
        return self
    def display_account_info(self):
        # your code here
        # print to the console: eg. "Balance: $100"
        print("Account intrest rate:", self.int_rate)
        print("Balance:", self.balance)
    def yield_interest(self):
        # your code here
        # increases the account balance 
        # by the current balance * the interest rate (as long as the balance is positive)
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        else:
            print("Insufficient balance: Intrest could not apply")
        return self

account1 = BankAccount(0.15, 1000)
account2 = BankAccount()

account1.deposit(500).deposit(500).withdraw(700).yield_interest().display_account_info()
account2.deposit(222).deposit(1230).withdraw(500).withdraw(100).withdraw(1000).withdraw(100).yield_interest().display_account_info()