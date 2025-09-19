# amount_paid, 
# amount_remaining, 

class Loan:
    def __init__(self, name, loan_amount, duration, gender):
        self.name = name
        self.loan_amount = loan_amount
        self.duration = duration
        self.gender = gender

    def check_gender(self):
        if self.gender.lower() == 'male':
            return "HIS", "HE", "MR."       # these here are being returned as touple ("HIS", "HE", "MR.")
        else:
            return "HER", "SHE", "MS."

    def data(self):
        if self.loan_amount == 0:
            print(f"LOAN IS ALREADY SETTLED")

        print(f"""
        NAME            : {self.name.upper()}
        LOAN AMOUNT     : {self.loan_amount}
        DURATION        : {self.duration}                
""")
             


class Accounts(Loan):               # one class can inherit multiple classes (class Accounts(Loan, another_class):) -- hence you can inherit multiple classes at the same time
    def pay(self, amount_paid):
        if self.loan_amount == 0:
            return f"LOAN IS ALREADY SETTLED"

        remaining = self.loan_amount - amount_paid
        self.loan_amount -= amount_paid

        his_her, he_she, title = self.check_gender()

        """
        ✅ When you write "self.check_gender()":
        Python will look for the method in the current class (Accounts). Since it’s not there, it goes up the inheritance chain and finds it in Loan. This works fine.

        ✅ When you write "super().check_gender()":
        This explicitly tells Python: “Call the method check_gender from the parent class (Loan) instead of looking for it in the child class first.”
        In this case, the output will be exactly the same, because Accounts hasn’t overridden check_gender().

        """
        
        if self.loan_amount <= 0:
            self.loan_amount = 0
            return f"{title}{self.name.upper()} HAS SETTLED {his_her} LOAN COMPLETELY."

        return (f"{title}{self.name.upper()} HAS PAID AMOUNT {amount_paid}. "
                f"REMAINING LOAN AMOUNT = {remaining}")

    def more_loan(self, more_amount):
        old_amount = self.loan_amount
        self.loan_amount += more_amount

        his_her, he_she, title = self.check_gender()        # in the oreder ("HIS", "HE", "MR.") are being rerturned in the same order they will be stored into -- his_her, he_she, title

        return (f"THE ACCOUNT HOLDER REQUIRES MORE LOAN\n"
                f"{title}{self.name.upper()} HAD A LOAN OF {old_amount}.\n"
                f"{he_she} REQUIRES MORE LOAN OF {more_amount}.\n"
                f"TOTAL LOAN AMOUNT NOW = {self.loan_amount}")


print("*******************************************************************************************")

p1 = Accounts('Simran Gupta', 12000, 3, 'female')

p1.data()
print("*******************************************************************************************")

print(p1.more_loan(5000))
print("*******************************************************************************************")
print(p1.pay(10000))
print("*******************************************************************************************")
print(p1.pay(7000))

print("*******************************************************************************************")
p1.data()
print("*******************************************************************************************")
