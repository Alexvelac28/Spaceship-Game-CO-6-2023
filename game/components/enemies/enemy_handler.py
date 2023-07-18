from game.components.enemies.ship import Ship
from game.components.enemies.ovni import Ovni
from game.components.enemies.galactic import Galactic
from game.components.enemies.droid import Droid
from game.components.enemies.stellar import Stellar
from game.components.enemies.hunter import Hunter

class Enemyhandler:
    def __init__(self):
        self.enemies = []

    def update(self, bullet_handler):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(bullet_handler)
            if not enemy.is_visible:
                self.remove_enemy(enemy)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < 2:
            self.enemies.append(Ship())
        if len(self.enemies) < 3:
            self.enemies.append(Ovni())
        if len(self.enemies) < 5:
            self.enemies.append(Galactic())
        if len(self.enemies) < 5:
            self.enemies.append(Droid())
        if len(self.enemies) < 7:
            self.enemies.append(Stellar())

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)