#Day4
#Question 1 :
#Create a bank account system with the ability to create/ close an account, deposit, withdraw, etc.. Using OOPs concepts.
class BankAcc:
    def __init__(self, acc_id, acc_name, bal=0):
        self.acc_id = acc_id
        self.acc_name = acc_name
        self.bal = max(bal, 0)
        self.is_active = True
    def dep(self, amt):
        if self.is_active and amt > 0:
            self.bal += amt
            print("₹",amt," deposited. New Balance: ₹",self.bal)
        else:
            print("Deposit failed. Check amount and account status.")
    def wth(self, amt):
        if not self.is_active:
            print("Withdrawal failed. Account inactive.")
        elif amt > 0 and amt <= self.bal:
            self.bal -= amt
            print("₹",amt," withdrawn. New Balance: ₹",self.bal)
        else:
            print("Invalid withdrawal amount or insufficient funds.")
    def chk_bal(self):
        if self.is_active:
            print("Balance: ₹",self.bal)
        else:
            print("Account inactive. Cannot display balance.")
    def cls_acc(self):
        if self.is_active:
            self.is_active = False
            print("Account",self.acc_id," is closed. Final Balance: ₹",self.bal)
        else:
            print("Account already inactive.")
    def reopen(self):
        if not self.is_active:
            self.is_active = True
            print("Account ",self.acc_id," reopened.")
        else:
            print("Account is already active.")
    def transfer(self, other, amt):
        if self.is_active and other.is_active:
            if amt > 0 and amt <= self.bal:
                self.bal -= amt
                other.bal += amt
                print("₹",amt," transferred from Acc ",self.acc_id," to Acc ",other.acc_id)
            else:
                print("Transfer failed. Check amount or balance.")
        else:
            print("Transfer failed. One or both accounts inactive.")
class BankSys:
    def __init__(self):
        self.acc_list = {}
    def create_acc(self, acc_id, acc_name, init_bal=0):
        if acc_id not in self.acc_list:
            self.acc_list[acc_id] = BankAcc(acc_id, acc_name, init_bal)
            print("Account",acc_id," created for ",acc_name," with ₹",init_bal)
        else:
            print("Account ",acc_id," already exists.")
    def get_acc(self, acc_id):
        return self.acc_list.get(acc_id, None)
    def all_accs(self):
        for acc_id, acc in self.acc_list.items():
            status = "Active" if acc.is_active else "Inactive"
            print("Acc ",acc_id,"Name: ",acc.acc_name," Balance: ₹",acc.bal," Status: ",status)
def menu():
    bank = BankSys()
    repeat=1
    while repeat==1:
        print("Bank Account System Menu")
        print()
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Close Account")
        print("6. Reopen Account")
        print("7. Transfer Money")
        print("8. Display All Accounts")
        print("9. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":  
            acc_id = int(input("Enter Account ID: "))
            acc_name = input("Enter Account Holder Name: ")
            init_bal = float(input("Enter Initial Balance: "))
            bank.create_acc(acc_id, acc_name, init_bal)
        elif choice == "2":  
            acc_id = int(input("Enter Account ID: "))
            acc = bank.get_acc(acc_id)
            if acc:
                amt = float(input("Enter Amount to Deposit: "))
                acc.dep(amt)
            else:
                print("Account not found.")
        elif choice == "3":  
            acc_id = int(input("Enter Account ID: "))
            acc = bank.get_acc(acc_id)
            if acc:
                amt = float(input("Enter Amount to Withdraw: "))
                acc.wth(amt)
            else:
                print("Account not found.")
        elif choice == "4":  
            acc_id = int(input("Enter Account ID: "))
            acc = bank.get_acc(acc_id)
            if acc:
                acc.chk_bal()
            else:
                print("Account not found.")
        elif choice == "5":  
            acc_id = int(input("Enter Account ID: "))
            acc = bank.get_acc(acc_id)
            if acc:
                acc.cls_acc()
            else:
                print("Account not found.")
        elif choice == "6":  
            acc_id = int(input("Enter Account ID: "))
            acc = bank.get_acc(acc_id)
            if acc:
                acc.reopen()
            else:
                print("Account not found.")
        elif choice == "7": 
            from_id = int(input("Enter Sender Account ID: "))
            to_id = int(input("Enter Receiver Account ID: "))
            amt = float(input("Enter Amount to Transfer: "))
            from_acc = bank.get_acc(from_id)
            to_acc = bank.get_acc(to_id)
            if from_acc and to_acc:
                from_acc.transfer(to_acc, amt)
            else:
                print("One or both accounts not found.")
        elif choice == "8": 
            bank.all_accs()
        elif choice == "9":
            repeat=0
            print("Exited!")
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    menu()
