from project.player.player import Player


class BattleField:
    @staticmethod
    def fight(attacker: Player, enemy: Player):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")

        # If a player is a beginner, increase his health with 40 points and increase the damage points of each card in the players' deck with 30.
        if attacker.__class__.__name__ == "Beginner":
            attacker.health += 40
            for card in attacker.card_repository.cards:
                card.damage_points += 30

        if enemy.__class__.__name__ == "Beginner":
            attacker.health += 40
            for card in enemy.card_repository.cards:
                card.damage_points += 30

        attacker.health += sum([card.health_points for card in attacker.card_repository.cards])
        enemy.health += sum([card.health_points for card in enemy.card_repository.cards])

        for card in attacker.card_repository.cards:
            enemy.take_damage(card.damage_points)

        for card in enemy.card_repository.cards:
            attacker.take_damage(card.damage_points)
