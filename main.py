from Account import *

oJoesAccount: Account = Account("Joe", 100000, 'ewfi3r3213d2')
# print("Created an account for Joe")

oMaryAccount: Account = Account("Mary", 800000, 'sdkj29e2')
# print("Created an account for Joe")

# oJoesAccount.show()
# oMaryAccount.show()
# print()

#Calling methods for the two accounts
if (q := oJoesAccount.deposit(1000, "ewfi3r3213d2")) != None:
    print("Current balance: ", q)
# oMaryAccount.deposit(8000, "sdkj29e2")
