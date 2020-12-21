import pygame, os
from .constants import *
import time
class piece:
    black_attacks = []
    best_move = [0, 0, 0, 0, 0]
    pressed = False
    possible_moves = []
    current = []
    skip = False
    black_dead = []
    white_dead = []
    white_alive = []
    black_alive = []
    possible_attacks = []

    root_pawn_attacks = []
    root_pawn_moves = []

    root_king_attacks = []
    root_king_moves = []

    root_queen_attacks = []
    root_queen_moves = []

    root_horse_attacks = []
    root_horse_moves = []

    root_bishop_attacks = []
    root_bishop_moves = []

    root_rook_attacks = []
    root_rook_moves = []

    white_root_pawn_attacks = []
    white_root_pawn_moves = []

    white_root_king_attacks = []
    white_root_king_moves = []

    white_root_queen_attacks = []
    white_root_queen_moves = []

    white_root_horse_attacks = []
    white_root_horse_moves = []

    white_root_bishop_attacks = []
    white_root_bishop_moves = []

    white_root_rook_attacks = []
    white_root_rook_moves = []
    def __init__(self, color, row, col, type1):

        self.color = color
        self.row = row
        self.col = col

        self.type1 = type1
        if self.color == BLACK:
            self.direction =1
        else:
            self.direction = -1
        self.x = 0
        self.y = 0
        self.calc_pos()
        if type1 == "pawnb" or type1 == "pawnw":
            self.first_move = True

    def calc_pos(self):
        self.x = self.row * SQUARE_SIZE  + 50
        self.y= self.col * SQUARE_SIZE + 50
        self.xpic =self.row * SQUARE_SIZE
        self.ypic =self.col * SQUARE_SIZE

    def draw(self, win):

        radius = SQUARE_SIZE // 2 - PADDING
        #pygame.draw.circle(win, GREY, (self.x  , self.y), 0)
        pygame.draw.circle(win, self.color, (self.x  , self.y), 0)
        # classes = np.array([["rook", "horse", "bishop", "queen", "king", "pawn", "none"], ["rookb", "horseb", "bishopb", "queenb", "kingb", "pawnb", "none"],])

        if self.type1 == classes[0][0]:
            #print("rook")
            win.blit(rookb, (self.xpic - 55, self.ypic - 25))
            pass
        elif self.type1 == classes[0][1]:
            win.blit(horseb, (self.xpic , self.ypic))
            #print("horse")
        elif self.type1 == classes[0][2]:
            #print("bishop")
            win.blit(bishopb, (self.xpic - 15, self.ypic))

        elif self.type1 == classes[0][3]:
            win.blit(queenb, (self.xpic - 70, self.ypic - 34))
            #print("queen")
        elif self.type1 == classes[0][4]:
            #print("king")
            win.blit(kingb, (self.xpic - 60, self.ypic - 13))

        elif self.type1 == classes[0][5]:
            #print("pawn")
            win.blit(pawnb, (self.xpic - 50, self.ypic ))
        elif self.type1 == classes[0][6]:
            #print("nothing")
            pass

        if self.type1 == classes[1][0]:
            #print("rook")
            win.blit(rookw, (self.xpic - 20, self.ypic - 0))
            pass
        elif self.type1 == classes[1][1]:
            win.blit(horsew, (self.xpic - 15, self.ypic))
            #print("horse")
        elif self.type1 == classes[1][2]:
            #print("bishop")
            win.blit(bishopw, (self.xpic - 15, self.ypic))

        elif self.type1 == classes[1][3]:
            win.blit(queenw, (self.xpic - 0, self.ypic - 0))
            #print("queen")
        elif self.type1 == classes[1][4]:
            #print("king")
            win.blit(kingw, (self.xpic - 7, self.ypic - 0))

        elif self.type1 == classes[1][5]:
            #print("pawn")
            win.blit(pawnw, (self.xpic - 0, self.ypic ))
        elif self.type1 == classes[1][6]:
            #print("nothing")
            pass


    #def move(self, moves, win):







