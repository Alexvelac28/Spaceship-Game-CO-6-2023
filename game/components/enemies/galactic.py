import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_3

class Galactic(Enemy):
    WIDTH = 45
    HEIGHT = 85

    def __init__(self):
        self.image = ENEMY_3
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)