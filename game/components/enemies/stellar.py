import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_5

class Stellar(Enemy):
    WIDTH = 60
    HEIGHT = 60
    SPEED_X = 4
    SPEED_Y = 3
    MOVEMENT_Y = 7
    MOVEMENT_X = 10
    INTERVAL = 80

    def __init__(self):
        self.image = ENEMY_5
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.index = 0
        super().__init__(self.image)

    def update(self):
        self.move_stellar()
        self.index += 1
        super().update()

    #def move_stellar(self):
     #   if self.index > self.INTERVAL:
    #        self.rect.y -= self.MOVEMENT_X
    #        self.rect.x -= self.MOVEMENT_Y