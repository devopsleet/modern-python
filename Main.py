from Enemy import *
from Zombie import *

def battle(e: Enemy):
    e.talk()
    e.attack()

zombie = Zombie(10, 1)
battle(zombie)
# print(zombie.get_type_of_enemy())
#
# print(zombie.talk())
#
# print(zombie.spread_disease())

# enemy.health_points = 10

# print(enemy.health_points)
# print(Enemy.health_points)

# enemy.type_of_enemy = "Gagan"

# print(f"{enemy.type_of_enemy} has {enemy.health_points} health points")

# print(enemy.talk())
# print(enemy.move_forward)
