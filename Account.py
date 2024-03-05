class Account:
    """Describes the account of a bank"""
    
    def __init__(self, name, balance, password) -> None:
        self.name = name
        self.balance = balance
        self.password = password

    def deposit(self, amountToDeposit, password):
        if password != self.password:
            print("Sorry, incorrect password")
            return None

        if amountToDeposit < 0:
            print("You cannot deposit a negative amount")
            return None

        self.balance = self.balance + amountToDeposit
        
        return self.balance
    
    def withdraw(self, amountToWithdraw, password):
        if password != self.password:
            print("Sorry, incorrect password")
            return None
        if amountToWithdraw < 0:
            print("You cannot withdraw a negative amount")    
            return None
        if amountToWithdraw > self.balance:
            print("You cannot withdraw more than you have in your account")
            return None
        
        self.balance = self.balance - amountToWithdraw
        return self.balance
    
    def getBalance(self, password):
        if password != self.password:
            print("Sorry, incorrect password")
            return None
        
        return self.balance
    
    def show(self):
        """Shows the current data"""
        
        print("Name: ", self.name)
        print("Balance: ", self.balance)
        print()
        