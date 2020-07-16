import pygame as pg

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
LBROWN = (210, 180, 140)
BROWN = (139, 69, 19)

# game settings
WIDTH = 1024   # frame size, required to be multiplicable by 32 and 64
HEIGHT = 768  # frame size, required to be multiplicable by 32 and 64
FPS = 60
TITLE = "fire" # name of game window
BGCOLOR = LBROWN

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

WALL_IMG = 'tile_205.png'

# Player settings
PLAYER_HEALTH = 100
PLAYER_SPEED = 250
PLAYER_ROT_SPEED = 250
PLAYER_IMG = 'manBrown_hold.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 40, 40)

# Fist settings
FIST_IMG = 'fist_particles.png'
FIST_SPEED = 400
FIST_LIFETIME = 100
FIST_RATE = 500
KNOCKBACK = 200
FIST_ACCURACY = 5
FIST_DAMAGE = 10 # TODO: change damage to 40 and add invulnerability

# Mob settings
MOB_IMG = 'hitman1_gun.png'
MOB_SPEEDS = [200, 220, 225, 225, 240, 250]
MOB_HIT_RECT = pg.Rect(0, 0, 45, 45)
MOB_HEALTH = 100
MOB_DAMAGE = 25
MOB_KNOCKBACK = 50
AVOID_RADIUS = 90
