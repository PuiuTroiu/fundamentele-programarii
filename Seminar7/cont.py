class Cont:
    # def __init__(self,no: int, admin: str, amount: int = 0):
    #     self.no = no
    #     self.amount = amount
    #     self.admin = admin

    def __init__(self, amount: int = 0):
        self.amount = amount

    def plata(self,val):
        self.amount -= val

    def depundere(self,val):
        self.amount += val
