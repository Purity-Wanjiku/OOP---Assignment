class Account:
    bank="KCB"
    def __init__(self,type,services):
        self.type=type
        self.services=services
    def widthdraw(self):
        return f"This {self.bank} account can {self.services} money"
    def describe(self):
        return f"{self.bank} accounts have {self.type} discounts this month"
    def information(self):
        return f"A {self.type} account at {self.bank} can have {self.services}"