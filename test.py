from pokemon import Pokemon, Trainer, Item, HealthPotion

charmander = Pokemon('Charmander', 10, 'Fire')
squirtle = Pokemon('Squirtle', 1, 'Water')
bulbasaur = Pokemon('Bulbasaur', 1, 'Grass')
pokemon_list = [charmander, squirtle, bulbasaur]


potion = HealthPotion('Potion', 20)
item_list = [potion]


ash = Trainer('Ash', pokemon_list, item_list)


charmander.print_stats()

charmander.take_damage(50)

charmander.print_stats()

ash.use_item(potion)

charmander.print_stats()
