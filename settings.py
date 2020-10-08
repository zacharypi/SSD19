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
HEIGHT = 768   # frame size, required to be multiplicable by 32 and 64
FPS = 60
TITLE = "fire"  # name of game window
BGCOLOR = LBROWN

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

WALL_IMG = 'tile_205.png'

# Sounds
BG_MUSIC = 'lets_go_and_replay.ogg'
WEAPON_SOUNDS_PUNCH = ['hit-02.wav']
WEAPON_SOUNDS = {'fist': ['hit-02.wav'],
                 'beam': ['hit-02.wav'],
                 'pistol': ['hit-02.wav']
                }
ENEMY_HIT_SOUND = ['shoot-02.wav']
DEATH_SOUND = ['hit-03.wav']
ENEMY_DEATH_SOUND = ['hit-03.wav']
EFFECTS_SOUNDS = {'level_start': 'lets_go.ogg',
                  'health_up': 'pickup-03.wav',
                  'w_pickup': 'pickup-03.wav'}

# Player settings
PLAYER_HEALTH = 100
PLAYER_SPEED = 250
PLAYER_ROT_SPEED = 250
PLAYER_IMG = 'manBrown_hold.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 40, 40)

# Weapon settings
FIST_IMG = 'slash_04.png'
BULLET_IMG = 'circle_05.png'
WEAPONS = {}
WEAPONS['fist'] = {'attack_speed': 400,
                   'attack_lifetime': 100,
                   'attack_rate': 500,
                   'knockback': 200,
                   'accuracy': 5,
                   'damage': 10,
                   'attack_size': 'slash',
                   'attack_count': 1,
                   'punchthrough': 1,
                   'mob_knockback': 1
                  }
WEAPONS['beam'] = {'attack_speed': 1000,
                   'attack_lifetime': 500,
                   'attack_rate': 20,
                   'knockback': -200,
                   'accuracy': 60,
                   'damage': 0.6,
                   'attack_size': 'circ',
                   'attack_count': 5,
                   'punchthrough': 0,
                   'mob_knockback': -0.4
                  }
WEAPONS['pistol'] = {'attack_speed': 300,
                     'attack_lifetime': 4000,
                     'attack_rate': 900,
                     'knockback': -200,
                     'accuracy': 6,
                     'damage': 10,
                     'attack_size': 'circ',
                     'attack_count': 1,
                     'punchthrough': 0,
                     'mob_knockback': 0.5
                    }
FIST_SPEED = 400
FIST_LIFETIME = 100
FIST_RATE = 500
KNOCKBACK = 200
FIST_ACCURACY = 5
FIST_DAMAGE = 10  # TODO: change damage to 40 and add invulnerability

# Mob settings
MOB_IMG = 'hitman1_gun.png'
MOB_SPEEDS = [190, 200, 210, 210, 220, 220, 230, 240, 1000]
MOB_HIT_RECT = pg.Rect(0, 0, 45, 45)
MOB_HEALTH = 100
MOB_DAMAGE = 25
MOB_KNOCKBACK = 40
AVOID_RADIUS = 90
DETECT_RADIUS = 400

# Layers
BGEFFECTS_LAYER = 1
WALL_LAYER = 3
PLAYER_LAYER = 4
FIST_LAYER = 5
MOB_LAYER = 4
ITEM_LAYER = 2

# Items
ITEM_IMAGES = {'health': 'health_pack.png',
               'beam': 'circle_05.png',
               'fist': 'circle_05.png'
              }
HEALTH_PACK_AMOUNT = 25
BOB_RANGE = 10
BOB_SPEED = 0.6

# Effects
BLOOD_PARTICLES = ['B100.png', 'B101.png', 'B102.png']
SMOKE_DURATION = 5000
DAMAGE_ALPHA = [i for i in range(0, 255, 25)]
