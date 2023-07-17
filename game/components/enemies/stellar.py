import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_5

class Stellar(Enemy):
    WIDTH = 60
    HEIGHT = 60

    def __init__(self):
        self.image = ENEMY_5
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)