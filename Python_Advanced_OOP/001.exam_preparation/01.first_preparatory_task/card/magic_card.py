from project.card.card import Card


class MagicCard(Card):
    def __init__(self, name: str):  # конструктура
        super().__init__(name, damage_points=5, health_points=80)

# MagicCard
# Has 5 damage points and 80 health points.
# Constructor should take the following values upon initialization:
# name
