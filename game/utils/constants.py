import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))
F2 = pygame.image.load(os.path.join(IMG_DIR, 'Other/fondolf.png'))
FF = pygame.image.load(os.path.join(IMG_DIR, 'Other/fondol2.png'))
M = pygame.image.load(os.path.join(IMG_DIR, 'Other/Invasion.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/ovni.png"))
ENEMY_3 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/galactic.png"))
ENEMY_4 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/droid.png"))
ENEMY_5 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/stellar.png"))
ENEMY_6 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/hunter.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
EXPLOSION = pygame.image.load(os.path.join(IMG_DIR, "Other/explosion.png"))
TITULO = pygame.image.load(os.path.join(IMG_DIR, "Other/titulo.png"))

FONT_STYLE = 'freesansbold.ttf'


LEFT = 'left'
RIGTH = 'right'
BULLET_ENEMY_TYPE = 'enemy'
BULLET_SHIP = 'ship' 

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
