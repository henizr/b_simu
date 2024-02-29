class Account:
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