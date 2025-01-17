import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_4

class Droid(Enemy):
    WIDTH = 10
    HEIGHT = 20

    def __init__(self):
        self.image = ENEMY_4
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)