import pygame, os
import numpy as np
pygame.init()
# Constants
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS
PADDING = 10
OUTLINE = 2
#RGB
RED = (255, 0, 0)
BLUE = (0,0,255)
BLACK = (0,0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
GREEN = (0, 128, 0)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#images
current_path = os.path.dirname(__file__) # Where your .py file is located
resource_path = os.path.join(current_path, 'images') # The resource folder path
print(resource_path)
rookw = pygame.transform.scale(pygame.image.load(os.path.join(resource_path, 'rookw.png')), (130, 115))
rookb = pygame.transform.scale(pygame.image.load(os.path.join(resource_path, 'rookb.png')), (230,150))

horseb = pygame.transform.scale(pygame.image.load(os.path.join(resource_path, 'horseb.png')), (100, 100))
horsew = pygame.transform.scale(pygame.image.load(os.path.join(resource_path, 'horsew.png')), (130,100))

kingb = pygame.transform.scale(pygame.image.load(os.path.join(resource_path, 'kingb.png')), (230, 120))
kingw = pygame.transform.scale(pygame.image.load(os.path.join(resource_path, 'kingw.png')), (120,100))

queenb = pygame.transform.scale(pygame.image.load(os.path.join(resource_path, 'queenb.png')), (230, 150))
queenw = pygame.transform.scale(pygame.image.load(os.path.join(resource_path, 'queenw.png')), (110,100))

bishopb = pygame.transform.scale(pygame.image.load(os.path.join(resource_path, 'bishopb.png')), (130, 100))
bishopw = pygame.transform.scale(pygame.image.load(os.path.join(resource_path, 'bishopw.png')), (130,100))

pawnb = pygame.transform.scale(pygame.image.load(os.path.join(resource_path, 'pawnb.png')), (200, 120))
pawnw = pygame.transform.scale(pygame.image.load(os.path.join(resource_path, 'pawnw.png')), (100,100))


#classes
classes = np.array([["rookb", "horseb", "bishopb", "queenb", "kingb", "pawnb", "none"], ["rookw", "horsew", "bishopw", "queenw", "kingw", "pawnw", "none"],])

