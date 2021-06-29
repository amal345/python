class Bank_Account:
    def __init__(self,Account_number,Name,Type_of_account):
        self.acc_no=Account_number
        self.name=Name
        self.type_acc=Type_of_account
        self.blnc=0
    def deposite(self):
        amt=float(input("Enter the amount to deposite : "))
        self.blnc+=amt
        print("Amount Deposited : ",amt)
    def display(self):
        print("Account number : ",self.acc_no)
        print("Name : ",self.name)
        print("Type of Account : ",self.type_acc)
        print("Balance : ",self.blnc)
        print()
    def withdraw(self):
        amt=float(input("Enter the amount to withdraw : "))
        if(self.blnc>amt):
            self.blnc-=amt
            print("Amount Withdrawed : ",amt)
        else:
            print("Insufficient Balance")

a1=Bank_Account(10210,"Anu","Savings")
a1.display()
a1.deposite()
a1.display()
a1.withdraw()
a1.display()
