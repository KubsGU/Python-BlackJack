# Money.py


class Money:
    def __init__(self, amount):
        self.amount = amount

    def add_money(self,amount):
        self.amount += amount

    def check_amount(self, amount):
        if amount == 0:
            return self.amount > amount
        else:
            return self.amount >= amount

    def spend_money(self, amount):
        self.amount -= amount
