from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card: Card):
        if any(c.name == card.name for c in self.cards):
            raise ValueError(f"Card {card.name} already exists!")
        self.count += 1
        self.cards.append(card)

    def remove(self, card: str):
        if card == "":
            raise ValueError("Card cannot be an empty string!")

        search_card = [x for x in self.cards if x.name == card][0]
        self.cards.remove(search_card)
        self.count -= 1

    def find(self, name: str):
        search_name = [x for x in self.cards if x.name == name][0]
        return search_name
