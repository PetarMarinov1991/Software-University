from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str, pokemon_details=None):
        if pokemon_details is None:
            pokemon_details = []
        self.name = name
        self.pokemon_details = pokemon_details

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon.name in self.pokemon_details:
            return 'This pokemon is already caught'
        self.pokemon_details.append(pokemon.pokemon_details())
        return 'Caught ' + pokemon.pokemon_details()

    def release_pokemon(self, pokemon_name: str):
        for p in self.pokemon_details:
            if pokemon_name in p:
                self.pokemon_details.remove(p)
                return f'You have released {pokemon_name}'
            return 'Pokemon is not caught'

    def trainer_data(self):
        trainer_info = [
            f'Pokemon Trainer {self.name}',
            f'Pokemon count {len(self.pokemon_details)}'
        ]
        pokemon_info = [f'- {p}' for p in self.pokemon_details]

        return f'\n'.join(trainer_info + pokemon_info)
