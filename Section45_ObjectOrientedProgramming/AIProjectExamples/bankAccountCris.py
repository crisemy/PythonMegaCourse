class BankAccount:
    # Constructor of the Class
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        
    def get_depositing(self, deposit):
        self.balance += deposit
    
    def get_withdrawing(self, withdrawing):
        if (self.balance >= withdrawing):
            self.balance -= withdrawing
        else:
            print("Not enough founds")
    
    def get_accountBalance(self):
        return self.balance

# Constructing the Class
transac1 = BankAccount("Cris N.")
transac1.get_depositing(300.0)
print(f"The current balance is: {transac1.get_accountBalance()}")
transac1.get_withdrawing(200.0)
print(f"The current balance is: {transac1.get_accountBalance()}")
