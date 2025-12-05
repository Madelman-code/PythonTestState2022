class Character:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def set_name(self, name):
        self.name = name
    
    def set_id(self, id):
        self.id = id
    
    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.id
    
class Hero(Character):
    def __init__(self, name, id, level, loot):
        super().__init__(name, id)
        self.level = level
        self.loot = loot
    
    def set_level(self, level):
        self.level = level
    
    def get_level(self):
        return self.level
    
    def set_loot(self, loot):
        self.loot = loot
    
    def get_loot(self):
        return self.loot
    
    def get_name(self):
        return self.name
    

class Boss(Character):
    def __init__(self, name, id, level, hp, attack_damage):
        super().__init__(name, id)
        self.level = level
        self.hp = hp
        self.attack_damage = attack_damage
        self.lifespan = 0
    
    def set_level(self, level):
        self.level = level
    
    def set_hp(self, hp):
        self.hp = hp

    def set_attack_damage(self, attack_damage):
        self.attack_damage = attack_damage
    
    def set_lifespan(self, lifespan):
        self.lifespan = lifespan
    
    def get_level(self):
        return self.level
    def get_hp(self):
        return self.hp
    def get_attack_damage(self):
        return self.attack_damage
    def get_lifespan(self):
        return (self.hp / 300)
    