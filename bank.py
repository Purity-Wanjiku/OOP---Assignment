class Account:
    bank="KCB"
    def __init__(self,type,services,balance):
        self.type=type
        self.services=services
        self.deposits = []
        self.withdrawals = []
        self.loan_balance=0
        self.balance = balance
        
    def widthdrawal(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            self.withdrawals.append({"amount":amount,"narration":"withdrawal"})
            return True
        else:
            return False
    
    def describe(self):
        return f"{self.bank} accounts have {self.type} discounts this month"
    def information(self):
        return f"A {self.type} account at {self.bank} can have {self.services}"
    def check_balance(self):
        return f"Your current balance is {self.balance}"
    def deposit(self,amount):
        self.balance += amount
        transaction = {"amount":amount,"narration":"deposits"}
        self.deposits.append(transaction)
        return f"money deposited successfully."
    def print_statement(self):
        combined_list=self.deposits+self.withdrawals
        print(combined_list)
        for c in combined_list:
            print(f"{c['narration']} - {c['amount']}")
    def borrow_loan(self,amount):
           if self.loan_balance > 0
              return f"There is an outstanding balance of {self.loan_balance}"
           elif amount<100:
             return "loan limit must not exceed 100"
           elif len(self.deposit)<100:
            return f"the number "
    
           total_deposits=sum([transaction["amount"]for transaction in self.deposits])
           limit =total_deposits/3
           if amount<=limit:
                   self.loan_balance+=amount
                   print ("Loan successfuly borrowed ")
           elif:
                   print ("Loan borrowed exceeds limit")
           else:
             print("Loan does not meet requirements")
 
    def repay_loan(self,amount):
        if amount > self.loan_balance:
            diff = amount - self.loan_balance
            self.loan_balance = 0
            self.balance += diff
            return  ""
        else:
            self.loan_balance -= amount
            self.balance += amount
            
            
    
            
        
        
        
    