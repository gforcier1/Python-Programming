from dataclasses import dataclass

@dataclass
class Gamer:
    gamer_id:int = 0
    name:str = ""
    health:int = 0
    weapon_id:int = 0
    location_id:int = 0
    weapon_name:str = ""
    weapon_damage:int = 0
    location_name:str = ""
    enemy_health:int = 0
    gold:int = 0

    @property
    def getStart(self):
        return f"{self.name} HP:{self.health} Location: {self.location_name}"

    @property
    def getDefeat(self):
        return f"You're health is gone. You've collected {self.gold} gold"

    @property
    def getWeapon(self):
        return f"Weapon: {self.weapon_name} Damage: {self.weapon_damage}"

    @property
    def getLocation(self):
        return f"You find yourself in the {self.location_name}. You pilfer {self.gold} gold!"

    @property
    def getEnemy(self):
        return f"You find an enemy with HP:{self.enemy_health}"
    @property
    def getStatus(self):
        return f"HP:{self.health} Weapon:{self.weapon_name} Damage:{self.weapon_damage} Location: {self.location_name}"

    def take_damage(self):
        damage = self.enemy_health // 3
        self.health -= damage
        print(f"{self.name} took {damage} damage")
        if self.health < 0:
            self.health = 0

    def heal(self, amount):
        self.health += amount

    def move_to(self, new_location_id, new_location_name, new_enemy_health, new_gold):
        self.location_id = new_location_id
        self.location_name = new_location_name
        self.enemy_health = new_enemy_health
        self.gold = new_gold

    def collect_gold(self, amount):
        self.gold += amount

    def is_alive(self):
        return self.health > 0


    
    
