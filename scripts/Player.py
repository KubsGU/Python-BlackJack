# Player.py
from scripts import Hand
from scripts import Money


class Player:
    def __init__(self, name, money):
        self.name = name
        self.points = 0
        self.hand = Hand.Hand()
        self.money = Money.Money(money)

    @property
    def calculate_points(self):
        self.points = self.hand.get_strength()
        return self.points

    def check_if_bankrupt(self):
        return not self.money.check_amount(0)

    def check_if_possible(self, amount):
        return self.money.check_amount(amount)

    def tell_the_money(self):
        return self.money.amount

    def make_bet(self, amount):
        self.money.spend_money(amount)

    def win_a_bet(self, amount):
        self.money.add_money(amount)


