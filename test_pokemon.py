from pokemon import Pokemon, Trainer, Item, HealthPotion

################################################################
### Pokemon
################################################################

charmander = Pokemon('Charmander', 10, 'Fire')
squirtle = Pokemon('Squirtle', 1, 'Water')
bulbasaur = Pokemon('Bulbasaur', 1, 'Grass')
growlithe = Pokemon('Growlithe', 1, 'Fire')
psyduck = Pokemon('Psyduck', 1, 'Water')
oddish = Pokemon('Oddish', 1, 'Grass')
fake_pokemon = Pokemon('Fake', 1, 'Normal')

pokemon_list_one = [charmander, squirtle, bulbasaur]
pokemon_list_two = [growlithe, psyduck, oddish]

################################################################
### Items
################################################################

potion = HealthPotion('Potion', 20)
super_potion = HealthPotion('Super Potion', 50)
hyper_potion = HealthPotion('Hyper Potion', 100)
item_list = [potion, super_potion, hyper_potion]

################################################################
### Trainers
################################################################

ash = Trainer('Ash', pokemon_list_one, item_list)
jen = Trainer('Jen', pokemon_list_two, item_list)

################################################################
### Tests
################################################################

ash.battle(jen)
