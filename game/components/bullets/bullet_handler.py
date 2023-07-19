from game.utils.constants import BULLET_ENEMY_TYPE, BULLET_SHIP
from game.components.bullets.bullet_enemy import BulletEnemy
from game.components.bullets.bullet_ship import BulletShip

class BulletHandler:
    def __init__(self):
        self.bullets = []

    def update(self, player, enemies):
        for bullet in self.bullets:
            if type(bullet) == BulletEnemy:
                bullet.update(player)
            elif type(bullet) == BulletShip:
                for enemy in enemies:
                    bullet.update(enemy)
            if not bullet.is_alive or not bullet.is_visible:
                self.remove_bullet(bullet) 

    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)

    def add_bullet(self, type, center):
        if type == BULLET_ENEMY_TYPE:
            self.bullets.append(BulletEnemy(center))
        elif type == BULLET_SHIP:
            self.bullets.append(BulletShip(center))

    def remove_bullet(self, bullet):
        self.bullets.remove(bullet)

    def reset(self):
        self.bullets = []