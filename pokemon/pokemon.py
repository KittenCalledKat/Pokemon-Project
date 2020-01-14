######################################################################
#### Pokemon Classes
######################################################################

class Pokemon():
    def __init__(self, pokemon, level, type, name=None, is_ko=False):
        self.pokemon = pokemon
        self.level = level
        self.max_health = self.level * 10
        self.health = self.max_health
        self.type = type
        self.is_ko = is_ko
        self.name = self.pokemon
        if name is not None:
            self.name = name

    def __repr__(self):
        return (
        f"\n{self.name} is a level {self.level} {self.type.lower()} type pokemon.")

    def print_stats(self):
        print(
        f'Here are {self.name}\'s current stats: \n'
        '\n'
        f'Level: {self.level} \n'
        f'Current Health: {self.health} \n'
        f'Max Health: {self.max_health} \n'
        f'Type: {self.type} \n'
        f'Knocked Out?: {self.is_ko} \n')

    def take_damage(self, damage_amount):
        self.health -= damage_amount
        if self.health <= 0:
            self.is_ko = True
            self.health =  0
            print(f"{self.name} took too much damage and is knocked out! \n")
        else:
            print(f"{self.name} took {damage_amount} points of damage and has {self.health}/{self.max_health} remaining. \n")
    def add_health(self, hp):
        self.health += hp
        if self.health > self.max_health:
            self.health = self.max_health

    def revive(self):
        if self.is_ko == True:
            self.is_ko = False
            self.health = self.max_health
            print(f"{self.name} has been revived and their health is {self.health}/{self.max_health}.\n")
        else:
            print(f"{self.name}'s is not knocked out, so they cannot be revived.\n")

    def is_very_effective(self, target):
        if self.type == 'Fire' and target.type == 'Grass':
            return True
        if self.type == 'Water' and target.type == 'Fire':
            return True
        if self.type == 'Grass' and target.type == 'Water':
            return True
        return False

    def is_weak_attack(self, target):
        if self.type == 'Grass' and target.type == 'Fire':
            return True
        if self.type == 'Fire' and target.type == 'Water':
            return True
        if self.type == 'Water' and target.type == 'Grass':
            return True
        return False

    def attack(self, target):
        if self.is_very_effective(target):
            target.take_damage(self.level * 2)
            print(f"{self.name}'s attack was very effective!\n")
        elif self.is_weak_attack(target):
            target.take_damage(self.level / 2)
            print(f"{self.name}'s attack was not very effective!\n")
        else:
            target.take_damage(self.level)


######################################################################
#### Trainer Classes
######################################################################

class Trainer():
    def __init__(self, name, team, items):
        self.name = name
        self.team = team
        self.items = items
        self.current_pokemon = self.team[0]

    def __repr__(self):
        return (f"Here are {self.name}'s current stats:\n"
                "\n"
                f"Team: {self.team}\n"
                f"Items: {self.items}\n")

    def switch_pokemon(self, pokemon_one, pokemon_two):
        index_one = self.team.index(pokemon_one)
        index_two = self.team.index(pokemon_two)
        self.team[index_one], self.team[index_two] = self.team[index_two], self.team[index_one]
        print(f"Swapping {pokemon_one.name}'s place with {pokemon_two.name}. {pokemon_two.name} is now in postion {index_one + 1} and {pokemon_one.name} is in position {index_two + 1}")

    def use_item(self, item, pokemon=None):
        if pokemon is None:
            pokemon = self.team[0]
        if item in self.items:
            if pokemon != self.team[0]:
                index = self.team.index(pokemon)
                item.use(self.team[index])
            else:
                item.use(pokemon)
            index = self.items.index(item)
            self.items.pop(index)
            print(f"{self.name} used {item.name.lower()} on {pokemon.name}")
        else:
            print(f'Sorry, {self.name} doensn\'t have a {item.lower()} to use.')




######################################################################
#### Item Classes
######################################################################
class Item():
    def __init__(self, name, value):
        self.name = name
        self.value = value

class HealthPotion(Item):
    def use(self, pokemon):
        if pokemon.is_ko == True:
            print(f"{pokemon.name} is knocked out and must be revived first.")
        else:
            pokemon.add_health(self.value)









