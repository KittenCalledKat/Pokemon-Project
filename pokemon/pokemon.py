class Pokemon():
    def __init__(self, name, level, health, max_health, type, is_ko=False):
        self.name = name
        self.level = level
        self.health = health
        self.max_health = max_health
        self.type = type
        self.is_ko = is_ko

    def __repr__(self):
        return (
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

    def revive(self):
        if self.is_ko == True:
            self.is_ko = False
            self.health = self.max_health
            print(f"{self.name}'s heath has been restored to {self.health}/{self.max_health}.\n")
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
            print(f"{self.type} is very effective against {target.type} and did double damage!")
        elif self.is_weak_attack(target):
            target.take_damage(self.level / 2)
            print(f"{self.type} is not very effective against {target.type} and only did half damage!")
        else:
            target.take_damage(damage_amount)

