from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemon_details = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon.name in map(lambda x: x.name, self.pokemon_details):
            return 'This pokemon is already caught'
        self.pokemon_details.append(pokemon)
        return f'Caught {pokemon.pokemon_details()}'

    def release_pokemon(self, pokemon_name: str):
        pokemon = [p for p in self.pokemon_details if p.name == pokemon_name]
        if pokemon:
            self.pokemon_details.remove(pokemon[0])
            return f'You have released {pokemon_name}'
        return 'Pokemon is not caught'

    def trainer_data(self):
        result = f'Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon_details)}\n- '
        for pokemon in self.pokemon_details:
            result += pokemon.pokemon_details() + '\n'
        return result
