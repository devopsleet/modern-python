class Enemy:
    # type_of_enemy: str
    # health_points: int = 20
    # attack_damage: int

    def __init__(self, type_of_enemy, health_points, attack_damage):
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    def get_type_of_enemy(self):
        return self.__type_of_enemy

    def talk(self) -> None:
        return 'I am an enemy'

    def walk_forward(self):
        print(f"{self.type_of_enemy}")

    def attack(self):
        print(f'{self.attack_damage}')

    def special_attack(self):
        print('Enemy has no special attack')
