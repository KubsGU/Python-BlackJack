# Game.py
from scripts import Deck
from scripts import Player


class Game:

    def __init__(self, player):
        self.player = Player.Player(player, 500)
        self.dealer = Player.Player("Dealer", 1000000)
        self.deck = Deck.Deck()
        self.deck.shuffle()
        self.bet = 0

    def start_new_round(self):
        print("")
        print("_"*60)
        print("")
        self.player.hand.cards = []
        self.dealer.hand.cards = []
        print(f'Your balance is: {self.player.tell_the_money()}')
        self.deck = Deck.Deck()
        self.deck.shuffle()
        self.bet = 0
        self.deal_cards()

        while True:
            temp_bet = int(input("Make Your Bet: "))
            if self.player.check_if_possible(temp_bet):
                self.player.make_bet(temp_bet)
                self.bet = temp_bet * 2
                break
            else:
                print('Invalid value, try again\n')
        self.show_player_cards()
        self.show_dealer_cards(1)

        while True:
            if self.check_if_round_over():
                self.end_round()
                break
            else:
                temp_input = input("Type 'hit' or 'pass' ").lower()
                print("")
                if temp_input == "hit":
                    self.hit()
                elif temp_input == "pass":
                    self.dealer_plays()
                    self.end_round()
                    break
                else:
                    print('Invalid input, try again\n')

    def dealer_plays(self):
        self.show_dealer_cards()
        print("")
        while self.dealer.calculate_points < 17:
            if self.dealer.calculate_points > self.player.calculate_points:
                break
            card = self.deck.deal_one()
            self.dealer.hand.add_card(card)
        self.show_dealer_cards()

    def deal_cards(self):
        for i in range(0, 2):
            card_one = self.deck.deal_one()
            self.player.hand.add_card(card_one)
            card_two = self.deck.deal_one()
            self.dealer.hand.add_card(card_two)

    def show_player_cards(self):
        print("Players Cards: ")
        for card in self.player.hand.cards:
            print(f'{card} , ', end="")
        print(f"Player's score is: {self.player.calculate_points}")
        print(" ")

    def show_dealer_cards(self, no_of_cards=0):
        print("Dealers Cards: ")
        if no_of_cards == 0:
            for card in self.dealer.hand.cards:
                print(f'{card} , ', end="")
            print(f"Dealer's score is: {self.dealer.calculate_points}")

        else:
            for i in range(0, no_of_cards):
                print(f'{self.dealer.hand.cards[i]} , ')
        print(" ")

    def hit(self):
        card = self.deck.deal_one()
        self.player.hand.add_card(card)
        self.show_player_cards()
        self.show_dealer_cards(1)
        pass

    def game_result(self, result):
        if result == "Tie":
            self.player.win_a_bet(self.bet/2)
            print(f'Tie! your bet (${self.bet/2}) is returned to You!')

        elif result == "Win":
            self.player.win_a_bet(self.bet)
            print(f'Bravo! You won ${self.bet/2}!')

        elif result == "Lose":
            print(f'You lost ${self.bet/2}!')

        if self.player.check_if_bankrupt():
            print("You r bankrupt! Game over!")
        else:
            self.start_new_round()

    def end_round(self):
        if self.player.calculate_points < 21 and self.player.calculate_points == self.dealer.calculate_points:
            self.game_result("Tie")
            return
        if self.player.calculate_points > 21:
            self.game_result("Lose")
            return
        if self.dealer.calculate_points > 21:
            self.game_result("Win")
            return
        if self.player.calculate_points < self.dealer.calculate_points:
            self.game_result("Lose")
            return
        if self.player.calculate_points == 21:
            self.game_result("Win")
            return
        if 21 > self.player.calculate_points > self.dealer.calculate_points:
            self.game_result("Win")
            return

    def check_if_round_over(self):
        temp_score = self.player.calculate_points
        if temp_score >= 21:
            return True
        else:
            return False


if __name__ == '__main__':
    player_name = input("Provide player's name: ")
    game = Game(player_name)
    game.start_new_round()




