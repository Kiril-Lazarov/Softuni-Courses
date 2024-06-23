from pokemon import Pokemon

class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        return "This pokemon is already caught"

    def release_pokemon(self, name):
        for pokemon in self.pokemons:
            if pokemon.name == name:
                self.pokemons.remove(pokemon)
                return f"You have released {name}"

        return "Pokemon is not caught"

    def trainer_data(self):
        final_list = []
        final_list.append(f'Pokemon Trainer {self.name}')
        final_list.append(f'Pokemon count {len(self.pokemons)}')
        for name in self.pokemons:

            final_list.append(f'- {name.pokemon_details()}')
        return '\n'.join(final_list)




pokemon = Pokemon("Pikachu", 90)

print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())

