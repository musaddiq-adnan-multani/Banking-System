class Account ():
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance

    def display_details(self):
        return f"Account No: {self.account_number}, Balance: {self.balance}"

class SavingsAccount(Account):
    def __init__(self, account_no, balance, interest_rate):
        super().__init__(account_no, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        return interest
    def display_details(self):
        base_details = super().display_details() 
        return f"{base_details}, Interest Rate: {self.interest_rate}%"

class CurrentAccount(Account):
    def __init__(self, account_number, balance,overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit=overdraft_limit

    def display_details(self):
        base_details = super().display_details()
        return f"{base_details}, Overdraft Limit: {self.overdraft_limit}"
    

current = CurrentAccount("C456", 2000, 5000)
print(current.display_details())