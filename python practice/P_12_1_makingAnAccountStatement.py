# create an account class with 2 attributes - balance and account no.
# create methods for debit, credit, and printing the balance

class Account:
    
    def __init__(self, name, balance, accNo):
        self.name = name
        self.balance = balance
        self.accNo = accNo

    
    # debit
    def debit(self, amount):
        self.showDebit(amount, self.balance)
        self.balance -= amount
        return  self.balance

    def showDebit(self, amount, balance):
        print(f"AMOUNT {amount} HAS BEEN DEDUCTED FROM {balance} : REMAINING ({balance - amount})")

    
    # credit
    def credit(self, amount):
        self.showCredit(amount, self.balance)
        self.balance +=  amount
        return self.balance
    
    def showCredit(self, amount, balance):
        print(f"AMOUNT {amount} HAS BEEN CREDITED INTO {balance} : REMAINING ({balance + amount})")

    
    
    def show(self):
        print(f"""
    ACCOUNT HOLDER  : {self.name.upper()}
    ACCOUNT NO.     : {self.accNo}
    BALANCE         : {self.balance}
""")
        


a1 = Account('Biswajeet Pradhan', 10000, 12345678911)
a1.show()

a1.debit(3000)
# a1.show()

a1.credit(10000)
a1.show()

a1.credit(50000)
a1.credit(100000)
a1.debit(1000)





