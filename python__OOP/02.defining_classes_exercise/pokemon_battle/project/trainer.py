from pokemon_battle.project.pokemon import Pokemon
from typing import List


class Trainer:
    name: str
    pokemon: List[Pokemon]

    def __init__(self, name: str):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon in self.pokemon:
            return f'This pokemon is already caught'
        self.pokemon.append(pokemon)
        return f'Caught {pokemon.pokemon_details()}'

    def release_pokemon(self, pokemon_name: str) -> str:
        pokemon_to_be_deleted = [p for p in self.pokemon if p.name == pokemon_name]
        if not pokemon_to_be_deleted:
            return "Pokemon is not caught"
        searched_pokemon = pokemon_to_be_deleted[0]
        self.pokemon.remove(searched_pokemon)
        return f'You have released {pokemon_name}'

        # pokemon_names = [p.name for p in self.pokemon]
        # if not pokemon_names:
        #     return 'Pokemon is not caught'
        #
        # del self.pokemon[pokemon_name.index(pokemon_name)]
        # return f'You have released {pokemon_name}'

    def trainer_data(self):
        trainer_info = [
            f'Pokemon Trainer {self.name}\n'
            f'Pokemon count {len(self.pokemon)}'
        ]
        pokemon_info = [f"- {p.pokemon_details()}" for p in self.pokemon]

        return '\n'.join(trainer_info + pokemon_info)


"""
"Pokemon Trainer {trainer_name}
 Pokemon count {the amount of pokemon caught}
 - {pokemon_details}
 ...
 - {pokemon_details}
"

"""

pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
