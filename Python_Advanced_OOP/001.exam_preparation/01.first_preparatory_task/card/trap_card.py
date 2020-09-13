from project.card.card import Card


class TrapCard(Card):
    def __init__(self, name: str):  # конструктура
        super().__init__(name, damage_points=120, health_points=5)

# TrapCard
# Has 120 damage points and 5 health points.
# Constructor should take the following values upon initialization:
# name
