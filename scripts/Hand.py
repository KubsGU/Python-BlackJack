# Hand.py


class Hand:

    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def count_cards_by_rank(self, rank):
        return len(list(filter(lambda x: x.rank == rank, self.cards)))

    def get_strength(self):
        no_of_aces = self.count_cards_by_rank("A")
        if no_of_aces == 2 and len(self.cards) == 2:
            score = 21
        else:
            score = 0
            for card in self.cards:
                score += card.value
            if len(self.cards) > 2 and no_of_aces > 1:
                for i in range(0, no_of_aces):
                    score -= 10
        return score
