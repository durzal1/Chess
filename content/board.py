#Board is 8x8 100px per square
from content.constants import *
from content.pieces import *
from content.ai_temp import *
import copy
import random
odd = {1,3, 5, 7}
even = [0, 2, 4 ,6]

odd1 = {"1","3", "5", "7"}
even1 = ["0", "2", "4", "6", "8"]


class Board:

    def __init__(self):
        self.board = []
        self.board_temp = []
        self.board_temp1 = []
        self.all_white_attacks = []
        self.create_board()
        clicked = False
        self.black_attacks = []
        self.turn = 1
        self.turn_color = (0,0, 0)
        self.turn_over = True
        self.check = False

    def __repr__(self):
        return self.board1


    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(8):
            if row in even:
                for col in range(0, 8, 2):
                    # print(row, col)
                    pygame.draw.rect(win, RED, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            if row in odd:
                for col in range(1, 8, 2):
                    # print(row, col)
                    pygame.draw.rect(win, RED, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    def create_board(self):
        for row in range(8):
            self.board.append([])
            for col in range(8):
                global color_1



                if col == 0:
                    if row == 0:
                        #classes = ["rook", "horse", "bishop", "king", "queen", "pawn"]
                        type1 = classes[0][0]

                    elif row == 1:
                        type1 = classes[0][1]
                    elif row == 2:
                        type1 = classes[0][2]
                    elif row == 3:
                        type1 = classes[0][3]
                    elif row == 4:
                        type1 = classes[0][4]
                    elif row == 5:
                        type1 = classes[0][2]
                    elif row == 6:
                        type1 = classes[0][1]
                    elif row == 7:
                        type1 = classes[0][0]
                    color_1 = BLACK
                    #self.board[row].append(piece(BLACK, row, col, type1))
                if col == 7:
                    if row == 0:
                        #classes = ["rook", "horse", "bishop", "king", "queen", "pawn"]
                        type1 = classes[1][0]

                    elif row == 1:
                        type1 = classes[1][1]
                    elif row == 2:
                        type1 = classes[1][2]
                    elif row == 3:
                        type1 = classes[1][3]
                    elif row == 4:
                        type1 = classes[1][4]
                    elif row == 5:
                        type1 = classes[1][2]
                    elif row == 6:
                        type1 = classes[1][1]
                    elif row == 7:
                        type1 = classes[1][0]
                    color_1 = WHITE
                    #self.board[row].append(piece(WHITE, row, col, type1))
                if col == 1:
                    type1 = classes[0][5]
                    color_1 = BLACK

                    #self.board[row].append(piece(BLACK, row, col, type1))
                if col == 6:
                    type1 = classes[1][5]
                    color_1 = WHITE

                    #self.board[row].append(piece(WHITE, row, col, type1))
                if  1 < col < 6:
                    type1 = classes[1][6]
                    color_1 = GREEN


                self.board[row].append(piece(color_1, row, col, type1)) #IF I WANT THE NO SPACES TO HAVE A VAL
                if color_1 == WHITE:
                    piece.white_alive.append(f" {type1}") #IF I WANT THE NO SPACES TO HAVE A VAL
                elif color_1 == BLACK:
                    piece.black_alive.append(f"{type1}")







        #print(self.board[1][0].type1) # row is listing x and col is listing y
        #print(self.board[3][7].type1)

    def draw_piece(self, win):

        for row in range(8):
            for col in range(8):

                if self.board[row][col] != 0:
                    piece_draw = self.board[row][col]


                    piece_draw.draw(win)


    def mouse_pressed(self, pos, win):
        x1 = pos[0]
        y1 = pos[1]
        win = win
        col_press = y1 // SQUARE_SIZE
        row_press = x1 // SQUARE_SIZE
        print("======================================")
        #print(row_press, col_press)
        #print((self.board[1][0].row,self.board[1][0].col))  # row is listing x and col is listing y
        #print(self.board[3][0].type1)  # row is listing x and col is listing y
        type_piece = (self.board[row_press][col_press].type1)  # row is listing x and col is listing y
        color_piece = (self.board[row_press][col_press].color)  # row is listing x and col is listing y
        self.setup( type_piece, row_press, col_press,color_piece,self.turn, win )



    def setup(self, type2, row, column, color, turn,  win):
        global pressed
        #print(type_piece1)
        type_piece = type2
        row1 = row
        column1 = column
        color1 = color
        turn = turn
        win = win
        x = row1 * SQUARE_SIZE + 50
        y = column1 * SQUARE_SIZE + 50
        diff = 100
        possible_moves = []
        print("--------------")
        print(row, column)
        print("--------------")

        if not(piece.skip):
            if not(piece.pressed):
                if type_piece == classes[1][0]:
                    print("rookw")
                    if self.turn_color == (255, 255, 255):
                        for i in range(8):
                            # add 100 to y
                            row = row
                            new_col = column1 + i + 1
                            if row > 7 or new_col > 7:
                                break
                            if self.board[row][new_col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x, y + (diff * i) + diff), 20)
                                piece.possible_moves.append((str(row), str(new_col), int(x), int(y + (diff * i) + diff)))
                                piece.white_root_rook_moves.append([str(row), str(new_col), int(x), int(y + (diff * i) + diff)])
                            elif self.board[row][new_col].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, (x, y + (diff * i) + diff), 20)
                                piece.possible_attacks.append((str(row), str(new_col), int(x), int(y + (diff * i) + diff)))
                                piece.white_root_rook_attacks.append([str(row), str(new_col), int(x), int(y + (diff * i) + diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            # subtract 100 to y
                            row = row
                            new_col = column1 - i - 1
                            if row > 7 or new_col > 7:
                                break
                            if self.board[row][new_col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x, y - (diff * i) - diff), 20)
                                piece.possible_moves.append((str(row), str(new_col), int(x), int(y - (diff * i) - diff)))
                                piece.white_root_rook_moves.append([str(row), str(new_col), int(x), int(y - (diff * i) - diff)])
                            elif self.board[row][new_col].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, (x, y - (diff * i) - diff), 20)
                                piece.possible_attacks.append((str(row), str(new_col), int(x), int(y - (diff * i) - diff)))
                                piece.white_root_rook_attacks.append([str(row), str(new_col), int(x), int(y - (diff * i) - diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            # add 100 to x
                            new_row = row + i + 1
                            col = column1
                            if new_row > 7 or col > 7:
                                break
                            if self.board[new_row][col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x + (diff * i) + diff, y), 20)
                                piece.possible_moves.append((str(new_row), str(col), int(x + (diff * i) + diff), int(y)))
                                piece.white_root_rook_moves.append([str(new_row), str(col), int(x + (diff * i) + diff), int(y)])
                            elif self.board[new_row][col].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, (x + (diff * i) + diff, y), 20)
                                piece.possible_attacks.append((str(new_row), str(col), int(x + (diff * i) + diff), int(y)))
                                piece.white_root_rook_attacks.append([str(new_row), str(col), int(x + (diff * i) + diff), int(y)])
                                break
                            else:
                                break
                        for i in range(8):
                            # subtract 100 to x
                            new_row = row - i - 1
                            col = column1
                            if new_row > 7 or col > 7:
                                break
                            if self.board[new_row][col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x - (diff * i) - diff, y), 20)
                                piece.possible_moves.append((str(new_row), str(col), int(x - (diff * i) - diff), int(y)))
                                piece.white_root_rook_moves.append([str(new_row), str(col), int(x - (diff * i) - diff), int(y)])
                            elif self.board[new_row][col].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, (x - (diff * i) - diff, y), 20)
                                piece.possible_attacks.append((str(new_row), str(col), int(x - (diff * i) - diff), int(y)))
                                piece.white_root_rook_attacks.append([str(new_row), str(col), int(x - (diff * i) - diff), int(y)])
                                break
                            else:
                                break

                        if len(piece.possible_moves) > 0 or len(piece.possible_attacks) > 0:
                            piece.current.extend([row, column])
                            piece.pressed = True
                elif type_piece == classes[0][0]:
                    print("rookb")
                    if self.turn_color == (0, 0, 0):
                        for i in range(8):
                            # add 100 to y
                            row = row
                            new_col = column1 + i + 1
                            if row > 7 or new_col > 7:
                                break
                            if self.board[row][new_col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x, y + (diff * i) + diff), 20)
                                piece.possible_moves.append((str(row), str(new_col), int(x), int(y + (diff * i) + diff)))
                                piece.root_rook_moves.append([str(row), str(new_col), int(x), int(y + (diff * i) + diff)])
                            elif self.board[row][new_col].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (x, y + (diff * i) + diff), 20)
                                piece.possible_attacks.append((str(row), str(new_col), int(x), int(y + (diff * i) + diff)))
                                piece.root_rook_attacks.append([str(row), str(new_col), int(x), int(y + (diff * i) + diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            # subtract 100 to y
                            row = row
                            new_col = column1 - i - 1
                            if row > 7 or new_col > 7:
                                break
                            if self.board[row][new_col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x, y - (diff * i) - diff), 20)
                                piece.possible_moves.append((str(row), str(new_col), int(x), int(y - (diff * i) - diff)))
                                piece.root_rook_moves.append([str(row), str(new_col), int(x), int(y - (diff * i) - diff)])
                            elif self.board[row][new_col].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (x, y - (diff * i) - diff), 20)
                                piece.possible_attacks.append((str(row), str(new_col), int(x), int(y - (diff * i) - diff)))
                                piece.root_rook_attacks.append([str(row), str(new_col), int(x), int(y - (diff * i) - diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            # add 100 to x
                            new_row = row + i + 1
                            col = column1
                            if new_row > 7 or col > 7:
                                break
                            if self.board[new_row][col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x + (diff * i) + diff, y), 20)
                                piece.possible_moves.append((str(new_row), str(col), int(x + (diff * i) + diff), int(y)))
                                piece.root_rook_moves.append([str(new_row), str(col), int(x + (diff * i) + diff), int(y)])
                            elif self.board[new_row][col].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (x + (diff * i) + diff, y), 20)
                                piece.possible_attacks.append((str(new_row), str(col), int(x + (diff * i) + diff), int(y)))
                                piece.root_rook_attacks.append([str(new_row), str(col), int(x + (diff * i) + diff), int(y)])
                                break
                            else:
                                break
                        for i in range(8):
                            # subtract 100 to x
                            new_row = row - i - 1
                            col = column1
                            if new_row > 7 or col > 7:
                                break
                            if self.board[new_row][col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x - (diff * i) - diff, y), 20)
                                piece.possible_moves.append((str(new_row), str(col), int(x - (diff * i) - diff), int(y)))
                                piece.root_rook_moves.append([str(new_row), str(col), int(x - (diff * i) - diff), int(y)])
                            elif self.board[new_row][col].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (x - (diff * i) - diff, y), 20)
                                piece.possible_attacks.append((str(new_row), str(col), int(x - (diff * i) - diff), int(y)))
                                piece.root_rook_attacks.append([str(new_row), str(col), int(x - (diff * i) - diff), int(y)])
                                break
                            else:
                                break

                        if len(piece.possible_moves) > 0 or len(piece.possible_attacks) > 0:
                            piece.current.extend([row, column])
                            piece.pressed = True

                elif type_piece == classes[1][1]:
                    print("horsew")
                    if self.turn_color == (255, 255, 255):
                        col = column

                        col_down1 = col + 1
                        col_down2 = col + 2
                        col_up1 = col - 1
                        col_up2 = col - 2

                        row_right1 = row + 1
                        row_right2 = row + 2
                        row_left1 = row - 1
                        row_left2 = row - 2
                        if row_right1 > 7 or row_right1 < 0 or col_down2 > 7 or col_down2 < 0:
                            pass
                        else:
                            if self.board[row_right1][col_down2].type1 == "none":
                                pygame.draw.circle(win, BLUE, (row_right1 * SQUARE_SIZE + 50, col_down2 * SQUARE_SIZE + 50),
                                                   20)
                                piece.possible_moves.append((str(row_right1), str(col_down2),
                                                             int(row_right1 * SQUARE_SIZE + 50),
                                                             int(col_down2 * SQUARE_SIZE + 50)))
                                piece.white_root_horse_moves.append([str(row_right1), str(col_down2),
                                                             int(row_right1 * SQUARE_SIZE + 50),
                                                             int(col_down2 * SQUARE_SIZE + 50)])
                            elif self.board[row_right1][col_down2].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN,
                                                   (row_right1 * SQUARE_SIZE + 50, col_down2 * SQUARE_SIZE + 50), 20)
                                piece.possible_attacks.append((str(row_right1), str(col_down2),
                                                               int(row_right1 * SQUARE_SIZE + 50),
                                                               int(col_down2 * SQUARE_SIZE + 50)))
                                piece.white_root_horse_attacks.append([str(row_right1), str(col_down2),
                                                               int(row_right1 * SQUARE_SIZE + 50),
                                                               int(col_down2 * SQUARE_SIZE + 50)])
                        if row_left1 > 7 or row_left1 < 0 or col_down2 > 7 or col_down2 < 0:
                            pass
                        else:
                            if self.board[row_left1][col_down2].type1 == "none":
                                pygame.draw.circle(win, BLUE, (row_left1 * SQUARE_SIZE + 50, col_down2 * SQUARE_SIZE + 50),
                                                   20)
                                piece.possible_moves.append((str(row_left1), str(col_down2),
                                                             int(row_left1 * SQUARE_SIZE + 50),
                                                             int(col_down2 * SQUARE_SIZE + 50)))
                                piece.white_root_horse_moves.append([str(row_left1), str(col_down2),
                                                             int(row_left1 * SQUARE_SIZE + 50),
                                                             int(col_down2 * SQUARE_SIZE + 50)])
                            elif self.board[row_left1][col_down2].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, (row_left1 * SQUARE_SIZE + 50, col_down2 * SQUARE_SIZE + 50),
                                                   20)
                                piece.possible_attacks.append([str(row_left1), str(col_down2),
                                                               int(row_left1 * SQUARE_SIZE + 50),
                                                               int(col_down2 * SQUARE_SIZE + 50)])
                                piece.white_root_horse_attacks.append([str(row_left1), str(col_down2),
                                                               int(row_left1 * SQUARE_SIZE + 50),
                                                               int(col_down2 * SQUARE_SIZE + 50)])
                        if row_left2 > 7 or row_left2 < 0 or col_down1 > 7 or col_down1 < 0:
                            pass
                        else:
                            if self.board[row_left2][col_down1].type1 == "none":
                                pygame.draw.circle(win, BLUE, (row_left2 * SQUARE_SIZE + 50, col_down1 * SQUARE_SIZE + 50),
                                                   20)
                                piece.possible_moves.append((str(row_left2), str(col_down1),
                                                             int(row_left2 * SQUARE_SIZE + 50),
                                                             int(col_down1 * SQUARE_SIZE + 50)))
                                piece.white_root_horse_moves.append([str(row_left2), str(col_down1),
                                                             int(row_left2 * SQUARE_SIZE + 50),
                                                             int(col_down1 * SQUARE_SIZE + 50)])
                            elif self.board[row_left2][col_down1].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, (row_left2 * SQUARE_SIZE + 50, col_down1 * SQUARE_SIZE + 50),
                                                   20)
                                piece.possible_attacks.append((str(row_left2), str(col_down1),
                                                               int(row_left2 * SQUARE_SIZE + 50),
                                                               int(col_down1 * SQUARE_SIZE + 50)))
                                piece.white_root_horse_attacks.append([str(row_left2), str(col_down1),
                                                               int(row_left2 * SQUARE_SIZE + 50),
                                                               int(col_down1 * SQUARE_SIZE + 50)])
                        if row_left2 > 7 or row_left2 < 0 or col_up1 > 7 or col_up1 < 0:
                            pass
                        else:
                            if self.board[row_left2][col_up1].type1 == "none":
                                pygame.draw.circle(win, BLUE, (row_left2 * SQUARE_SIZE + 50, col_up1 * SQUARE_SIZE + 50),
                                                   20)
                                piece.possible_moves.append((
                                                            str(row_left2), str(col_up1), int(row_left2 * SQUARE_SIZE + 50),
                                                            int(col_up1 * SQUARE_SIZE + 50)))
                                piece.white_root_horse_moves.append([str(row_left2), str(col_up1), int(row_left2 * SQUARE_SIZE + 50),
                                    int(col_up1 * SQUARE_SIZE + 50)])
                            elif self.board[row_left2][col_up1].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, (row_left2 * SQUARE_SIZE + 50, col_up1 * SQUARE_SIZE + 50),
                                                   20)
                                piece.possible_attacks.append((str(row_left2), str(col_up1),
                                                               int(row_left2 * SQUARE_SIZE + 50),
                                                               int(col_up1 * SQUARE_SIZE + 50)))
                                piece.white_root_horse_attacks.append([str(row_left2), str(col_up1),
                                                               int(row_left2 * SQUARE_SIZE + 50),
                                                               int(col_up1 * SQUARE_SIZE + 50)])
                        if row_left1 > 7 or row_left1 < 0 or col_up2 > 7 or col_up2 < 0:
                            pass
                        else:
                            if self.board[row_left1][col_up2].type1 == "none":
                                pygame.draw.circle(win, BLUE, (row_left1 * SQUARE_SIZE + 50, col_up2 * SQUARE_SIZE + 50),
                                                   20)
                                piece.possible_moves.append((
                                                            str(row_left1), str(col_up2), int(row_left1 * SQUARE_SIZE + 50),
                                                            int(col_up2 * SQUARE_SIZE + 50)))
                                piece.white_root_horse_moves.append([
                                    str(row_left1), str(col_up2), int(row_left1 * SQUARE_SIZE + 50),
                                    int(col_up2 * SQUARE_SIZE + 50)])
                            elif self.board[row_left1][col_up2].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, (row_left1 * SQUARE_SIZE + 50, col_up2 * SQUARE_SIZE + 50),
                                                   20)
                                piece.possible_attacks.append((str(row_left1), str(col_up2),
                                                               int(row_left1 * SQUARE_SIZE + 50),
                                                               int(col_up2 * SQUARE_SIZE + 50)))
                                piece.white_root_horse_attacks.append([str(row_left1), str(col_up2),
                                                               int(row_left1 * SQUARE_SIZE + 50),
                                                               int(col_up2 * SQUARE_SIZE + 50)])
                        if row_right1 > 7 or row_right1 < 0 or col_up2 > 7 or col_up2 < 0:
                            pass
                        else:
                            if self.board[row_right1][col_up2].type1 == "none":
                                pygame.draw.circle(win, BLUE, (row_right1 * SQUARE_SIZE + 50, col_up2 * SQUARE_SIZE + 50),
                                                   20)
                                piece.possible_moves.append((str(row_right1), str(col_up2),
                                                             int(row_right1 * SQUARE_SIZE + 50),
                                                             int(col_up2 * SQUARE_SIZE + 50)))
                                piece.white_root_horse_moves.append([str(row_right1), str(col_up2),
                                                             int(row_right1 * SQUARE_SIZE + 50),
                                                             int(col_up2 * SQUARE_SIZE + 50)])
                            elif self.board[row_right1][col_up2].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, (row_right1 * SQUARE_SIZE + 50, col_up2 * SQUARE_SIZE + 50),
                                                   20)
                                piece.possible_attacks.append((str(row_right1), str(col_up2),
                                                               int(row_right1 * SQUARE_SIZE + 50),
                                                               int(col_up2 * SQUARE_SIZE + 50)))
                                piece.white_root_horse_attacks.append([str(row_right1), str(col_up2),
                                                               int(row_right1 * SQUARE_SIZE + 50),
                                                               int(col_up2 * SQUARE_SIZE + 50)])
                        if row_right2 > 7 or row_right2 < 0 or col_up1 > 7 or col_up1 < 0:
                            pass
                        else:
                            if self.board[row_right2][col_up1].type1 == "none":
                                pygame.draw.circle(win, BLUE, (row_right2 * SQUARE_SIZE + 50, col_up1 * SQUARE_SIZE + 50),
                                                   20)
                                piece.possible_moves.append((str(row_right2), str(col_up1),
                                                             int(row_right2 * SQUARE_SIZE + 50),
                                                             int(col_up1 * SQUARE_SIZE + 50)))
                                piece.white_root_horse_moves.append([str(row_right2), str(col_up1),
                                                             int(row_right2 * SQUARE_SIZE + 50),
                                                             int(col_up1 * SQUARE_SIZE + 50)])
                            elif self.board[row_right2][col_up1].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, (row_right2 * SQUARE_SIZE + 50, col_up1 * SQUARE_SIZE + 50),
                                                   20)
                                piece.possible_attacks.append((str(row_right2), str(col_up1),
                                                               int(row_right2 * SQUARE_SIZE + 50),
                                                               int(col_up1 * SQUARE_SIZE + 50)))
                                piece.white_root_horse_attacks.append([str(row_right2), str(col_up1),
                                                               int(row_right2 * SQUARE_SIZE + 50),
                                                               int(col_up1 * SQUARE_SIZE + 50)])
                        if row_right2 > 7 or row_right2 < 0 or col_down1 > 7 or col_down1 < 0:
                            pass
                        else:
                            if self.board[row_right2][col_down1].type1 == "none":
                                pygame.draw.circle(win, BLUE, (row_right2 * SQUARE_SIZE + 50, col_down1 * SQUARE_SIZE + 50),
                                                   20)
                                piece.possible_moves.append((str(row_right2), str(col_down1),
                                                             int(row_right2 * SQUARE_SIZE + 50),
                                                             int(col_down1 * SQUARE_SIZE + 50)))
                                piece.white_root_horse_moves.append([str(row_right2), str(col_down1),
                                                             int(row_right2 * SQUARE_SIZE + 50),
                                                             int(col_down1 * SQUARE_SIZE + 50)])
                            elif self.board[row_right2][col_down1].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN,
                                                   (row_right2 * SQUARE_SIZE + 50, col_down1 * SQUARE_SIZE + 50), 20)
                                piece.possible_attacks.append([str(row_right2), str(col_down1),
                                                               int(row_right2 * SQUARE_SIZE + 50),
                                                               int(col_down1 * SQUARE_SIZE + 50)])
                                piece.white_root_horse_attacks.append([str(row_right2), str(col_down1),
                                                             int(row_right2 * SQUARE_SIZE + 50),
                                                             int(col_down1 * SQUARE_SIZE + 50)])
                        if len(piece.possible_moves) > 0 or len(piece.possible_attacks) > 0:
                            piece.current.extend([row, column])
                            piece.pressed = True
                elif type_piece == classes[0][1]:
                    print("horseb")
                    if self.turn_color == (0, 0, 0):
                        col = column




                        col_down1 = col + 1
                        col_down2 = col + 2
                        col_up1 = col - 1
                        col_up2 = col - 2

                        row_right1 = row + 1
                        row_right2 = row + 2
                        row_left1 = row - 1
                        row_left2 = row - 2
                        if row_right1 > 7 or row_right1 < 0 or col_down2 > 7 or col_down2 < 0:
                            pass
                        else:
                            if self.board[row_right1][col_down2].type1 == "none":
                                pygame.draw.circle(win, BLUE, (row_right1 * SQUARE_SIZE + 50, col_down2 * SQUARE_SIZE + 50), 20)
                                piece.possible_moves.append((str(row_right1), str(col_down2), int(row_right1 * SQUARE_SIZE + 50), int(col_down2 * SQUARE_SIZE + 50)))
                                piece.root_horse_moves.append([str(row_right1), str(col_down2), int(row_right1 * SQUARE_SIZE + 50), int(col_down2 * SQUARE_SIZE + 50)])
                            elif self.board[row_right1][col_down2].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (row_right1 * SQUARE_SIZE + 50, col_down2 * SQUARE_SIZE + 50), 20)
                                piece.possible_attacks.append((str(row_right1), str(col_down2), int(row_right1 * SQUARE_SIZE + 50), int(col_down2 * SQUARE_SIZE + 50)))
                                piece.root_horse_attacks.append([str(row_right1), str(col_down2), int(row_right1 * SQUARE_SIZE + 50), int(col_down2 * SQUARE_SIZE + 50)])
                        if row_left1 > 7 or row_left1 < 0 or col_down2 > 7 or col_down2 < 0:
                            pass
                        else:
                            if self.board[row_left1][col_down2].type1 == "none":
                                pygame.draw.circle(win, BLUE, (row_left1 * SQUARE_SIZE + 50, col_down2 * SQUARE_SIZE + 50), 20)
                                piece.possible_moves.append((str(row_left1), str(col_down2), int(row_left1 * SQUARE_SIZE + 50), int(col_down2 * SQUARE_SIZE + 50)))
                                piece.root_horse_moves.append([str(row_left1), str(col_down2), int(row_left1 * SQUARE_SIZE + 50), int(col_down2 * SQUARE_SIZE + 50)])
                            elif self.board[row_left1][col_down2].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (row_left1 * SQUARE_SIZE + 50, col_down2 * SQUARE_SIZE + 50), 20)
                                piece.possible_attacks.append((str(row_left1), str(col_down2), int(row_left1 * SQUARE_SIZE + 50), int(col_down2 * SQUARE_SIZE + 50)))
                                piece.root_horse_attacks.append([str(row_left1), str(col_down2), int(row_left1 * SQUARE_SIZE + 50), int(col_down2 * SQUARE_SIZE + 50)])
                        if row_left2 > 7 or row_left2 < 0 or col_down1 > 7 or col_down1 < 0:
                            pass
                        else:
                            if self.board[row_left2][col_down1].type1 == "none":
                                pygame.draw.circle(win, BLUE, (row_left2 * SQUARE_SIZE + 50, col_down1 * SQUARE_SIZE + 50), 20)
                                piece.possible_moves.append((str(row_left2), str(col_down1), int(row_left2 * SQUARE_SIZE + 50), int(col_down1 * SQUARE_SIZE + 50)))
                                piece.root_horse_moves.append([str(row_left2), str(col_down1), int(row_left2 * SQUARE_SIZE + 50), int(col_down1 * SQUARE_SIZE + 50)])
                            elif self.board[row_left2][col_down1].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (row_left2 * SQUARE_SIZE + 50, col_down1 * SQUARE_SIZE + 50), 20)
                                piece.possible_attacks.append((str(row_left2), str(col_down1), int(row_left2 * SQUARE_SIZE + 50), int(col_down1 * SQUARE_SIZE + 50)))
                                piece.root_horse_attacks.append([str(row_left2), str(col_down1), int(row_left2 * SQUARE_SIZE + 50), int(col_down1 * SQUARE_SIZE + 50)])
                        if row_left2 > 7 or row_left2 < 0 or col_up1 > 7 or col_up1 < 0:
                            pass
                        else:
                            if self.board[row_left2][col_up1].type1 == "none":
                                pygame.draw.circle(win, BLUE, (row_left2 * SQUARE_SIZE + 50, col_up1 * SQUARE_SIZE + 50), 20)
                                piece.possible_moves.append((str(row_left2), str(col_up1), int(row_left2 * SQUARE_SIZE + 50), int(col_up1 * SQUARE_SIZE + 50)))
                                piece.root_horse_moves.append([str(row_left2), str(col_up1), int(row_left2 * SQUARE_SIZE + 50), int(col_up1 * SQUARE_SIZE + 50)])
                            elif self.board[row_left2][col_up1].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (row_left2 * SQUARE_SIZE + 50, col_up1 * SQUARE_SIZE + 50), 20)
                                piece.possible_attacks.append((str(row_left2), str(col_up1), int(row_left2 * SQUARE_SIZE + 50), int(col_up1 * SQUARE_SIZE + 50)))
                                piece.root_horse_attacks.append([str(row_left2), str(col_up1), int(row_left2 * SQUARE_SIZE + 50), int(col_up1 * SQUARE_SIZE + 50)])
                        if row_left1 > 7 or row_left1 < 0 or col_up2 > 7 or col_up2 < 0:
                            pass
                        else:
                            if self.board[row_left1][col_up2].type1 == "none":
                                pygame.draw.circle(win, BLUE, (row_left1 * SQUARE_SIZE + 50, col_up2 * SQUARE_SIZE + 50), 20)
                                piece.possible_moves.append((str(row_left1), str(col_up2), int(row_left1 * SQUARE_SIZE + 50), int(col_up2 * SQUARE_SIZE + 50)))
                                piece.root_horse_moves.append([str(row_left1), str(col_up2), int(row_left1 * SQUARE_SIZE + 50), int(col_up2 * SQUARE_SIZE + 50)])
                            elif self.board[row_left1][col_up2].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (row_left1 * SQUARE_SIZE + 50, col_up2 * SQUARE_SIZE + 50), 20)
                                piece.possible_attacks.append((str(row_left1), str(col_up2), int(row_left1 * SQUARE_SIZE + 50), int(col_up2 * SQUARE_SIZE + 50)))
                                piece.root_horse_attacks.append([str(row_left1), str(col_up2), int(row_left1 * SQUARE_SIZE + 50), int(col_up2 * SQUARE_SIZE + 50)])
                        if row_right1 > 7 or row_right1 < 0 or col_up2 > 7 or col_up2 < 0:
                            pass
                        else:
                            if self.board[row_right1][col_up2].type1 == "none":
                                pygame.draw.circle(win, BLUE, (row_right1 * SQUARE_SIZE + 50, col_up2 * SQUARE_SIZE + 50), 20)
                                piece.possible_moves.append([str(row_right1), str(col_up2), int(row_right1 * SQUARE_SIZE + 50), int(col_up2 * SQUARE_SIZE + 50)])
                                piece.root_horse_moves.append([str(row_right1), str(col_up2), int(row_right1 * SQUARE_SIZE + 50), int(col_up2 * SQUARE_SIZE + 50)])
                            elif self.board[row_right1][col_up2].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (row_right1 * SQUARE_SIZE + 50, col_up2 * SQUARE_SIZE + 50), 20)
                                piece.possible_attacks.append((str(row_right1), str(col_up2), int(row_right1 * SQUARE_SIZE + 50), int(col_up2 * SQUARE_SIZE + 50)))
                                piece.root_horse_attacks.append([str(row_right1), str(col_up2), int(row_right1 * SQUARE_SIZE + 50), int(col_up2 * SQUARE_SIZE + 50)])
                        if row_right2 > 7 or row_right2 < 0 or col_up1 > 7 or col_up1 < 0:
                            pass
                        else:
                            if self.board[row_right2][col_up1].type1 == "none":
                                pygame.draw.circle(win, BLUE, (row_right2 * SQUARE_SIZE + 50, col_up1 * SQUARE_SIZE + 50), 20)
                                piece.possible_moves.append((str(row_right2), str(col_up1), int(row_right2 * SQUARE_SIZE + 50), int(col_up1 * SQUARE_SIZE + 50)))
                                piece.root_horse_moves.append([str(row_right2), str(col_up1), int(row_right2 * SQUARE_SIZE + 50), int(col_up1 * SQUARE_SIZE + 50)])
                            elif self.board[row_right2][col_up1].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (row_right2 * SQUARE_SIZE + 50, col_up1 * SQUARE_SIZE + 50), 20)
                                piece.possible_attacks.append((str(row_right2), str(col_up1), int(row_right2 * SQUARE_SIZE + 50), int(col_up1 * SQUARE_SIZE + 50)))
                                piece.root_horse_attacks.append([str(row_right2), str(col_up1), int(row_right2 * SQUARE_SIZE + 50), int(col_up1 * SQUARE_SIZE + 50)])
                        if row_right2 > 7 or row_right2 < 0 or col_down1 > 7 or col_down1 < 0:
                            pass
                        else:
                            if self.board[row_right2][col_down1].type1 == "none":
                                pygame.draw.circle(win, BLUE, (row_right2 * SQUARE_SIZE + 50, col_down1 * SQUARE_SIZE + 50), 20)
                                piece.possible_moves.append((str(row_right2), str(col_down1), int(row_right2 * SQUARE_SIZE + 50), int(col_down1 * SQUARE_SIZE + 50)))
                                piece.root_horse_moves.append([str(row_right2), str(col_down1), int(row_right2 * SQUARE_SIZE + 50), int(col_down1 * SQUARE_SIZE + 50)])
                            elif self.board[row_right2][col_down1].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (row_right2 * SQUARE_SIZE + 50, col_down1 * SQUARE_SIZE + 50), 20)
                                piece.possible_attacks.append((str(row_right2), str(col_down1), int(row_right2 * SQUARE_SIZE + 50), int(col_down1 * SQUARE_SIZE + 50)))
                                piece.root_horse_attacks.append([str(row_right2), str(col_down1), int(row_right2 * SQUARE_SIZE + 50), int(col_down1 * SQUARE_SIZE + 50)])
                        if len(piece.possible_moves) > 0 or len(piece.possible_attacks) > 0:
                            piece.current.extend([row, column])
                            piece.pressed = True

                elif type_piece == classes[1][2] :
                    print("bishopw")
                    if self.turn_color == (255, 255, 255):
                        for i in range(8):
                            # add 100 to y and x
                            new_row = row + i + 1
                            new_col = column1 + i + 1
                            if new_row > 7 or new_col > 7:
                                break
                            if self.board[new_row][new_col].type1 == "none":
                                pygame.draw.circle(win, BLUE, ((x + (diff * i) + diff), y + (diff * i) + diff), 20)
                                piece.possible_moves.append((str(new_row), str(new_col), int(x + (diff * i) + diff), int(y + (diff * i) + diff)))
                                piece.white_root_bishop_moves.append([str(new_row), str(new_col), int(x + (diff * i) + diff), int(y + (diff * i) + diff)])
                            elif self.board[new_row][new_col].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, ((x + (diff * i) + diff), y + (diff * i) + diff), 20)
                                piece.possible_attacks.append((str(new_row), str(new_col), int(x + (diff * i) + diff), int(y + (diff * i) + diff)))
                                piece.white_root_bishop_attacks.append([str(new_row), str(new_col), int(x + (diff * i) + diff), int(y + (diff * i) + diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            # subtract 100 to y and subtract 100 to x
                            new_row = row - i - 1
                            new_col = column1 - i - 1
                            if new_row > 7 or new_col > 7:
                                break
                            if self.board[new_row][new_col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x - (diff * i) - diff, y - (diff * i) - diff), 20)
                                piece.possible_moves.append((str(new_row), str(new_col), int(x - (diff * i) - diff), int(y - (diff * i) - diff)))
                                piece.white_root_bishop_moves.append([str(new_row), str(new_col), int(x - (diff * i) - diff), int(y - (diff * i) - diff)])
                            elif self.board[new_row][new_col].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, (x - (diff * i) - diff, y - (diff * i) - diff), 20)
                                piece.possible_attacks.append((str(new_row), str(new_col), int(x - (diff * i) - diff), int(y - (diff * i) - diff)))
                                piece.white_root_bishop_attacks.append([str(new_row), str(new_col), int(x - (diff * i) - diff), int(y - (diff * i) - diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            # add 100 to x and subtract 100 to y
                            new_row = row + i + 1
                            new_col = column1 - i - 1
                            if new_row > 7 or new_col > 7:
                                break
                            if self.board[new_row][new_col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x + (diff * i) + diff, y - (diff * i) - diff), 20)
                                piece.possible_moves.append((str(new_row), str(new_col), int(x + (diff * i) + diff), int(y - (diff * i) - diff)))
                                piece.white_root_bishop_moves.append([str(new_row), str(new_col), int(x + (diff * i) + diff), int(y - (diff * i) - diff)])
                            elif self.board[new_row][new_col].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, (x + (diff * i) + diff, y - (diff * i) - diff), 20)
                                piece.possible_attacks.append((str(new_row), str(new_col), int(x + (diff * i) + diff), int(y - (diff * i) - diff)))
                                piece.white_root_bishop_attacks.append([str(new_row), str(new_col), int(x + (diff * i) + diff), int(y - (diff * i) - diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            # subtract 100 to x and add 100 to y
                            new_row = row - i - 1
                            new_col = column1 + i + 1
                            if new_row > 7 or new_col > 7:
                                break
                            if self.board[new_row][new_col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x - (diff * i) - diff, y + (diff * i) + diff), 20)
                                piece.possible_moves.append((str(new_row), str(new_col), int(x - (diff * i) - diff), int(y + (diff * i) + diff)))
                                piece.white_root_bishop_moves.append([str(new_row), str(new_col), int(x - (diff * i) - diff), int(y + (diff * i) + diff)])

                            elif self.board[new_row][new_col].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, (x - (diff * i) - diff, y + (diff * i) + diff), 20)
                                piece.possible_attacks.append((str(new_row), str(new_col), int(x - (diff * i) - diff), int(y + (diff * i) + diff)))
                                piece.white_root_bishop_attacks.append([str(new_row), str(new_col), int(x - (diff * i) - diff), int(y + (diff * i) + diff)])
                                break
                            else:
                                break
                        if len(piece.possible_moves) > 0 or len(piece.possible_attacks) > 0:
                            piece.current.extend([row, column])
                            piece.pressed = True
                elif type_piece == classes[0][2]:
                    print("bishopb")
                    if self.turn_color == (0, 0, 0):
                        for i in range(8):
                            # add 100 to y and x
                            new_row = row + i + 1
                            new_col = column1 + i + 1
                            if new_row > 7 or new_col > 7:
                                break
                            if self.board[new_row][new_col].type1 == "none":
                                pygame.draw.circle(win, BLUE, ((x + (diff * i) + diff), y + (diff * i) + diff), 20)
                                piece.possible_moves.append(
                                    (str(new_row), str(new_col), int(x + (diff * i) + diff), int(y + (diff * i) + diff)))
                                piece.root_bishop_moves.append([str(new_row), str(new_col), int(x + (diff * i) + diff), int(y + (diff * i) + diff)])
                            elif self.board[new_row][new_col].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, ((x + (diff * i) + diff), y + (diff * i) + diff), 20)
                                piece.possible_attacks.append(
                                    (str(new_row), str(new_col), int(x + (diff * i) + diff), int(y + (diff * i) + diff)))
                                piece.root_bishop_attacks.append(
                                    [
                                    str(new_row), str(new_col), int(x + (diff * i) + diff), int(y + (diff * i) + diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            # subtract 100 to y and subtract 100 to x
                            new_row = row - i - 1
                            new_col = column1 - i - 1
                            if new_row > 7 or new_col > 7:
                                break
                            if self.board[new_row][new_col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x - (diff * i) - diff, y - (diff * i) - diff), 20)
                                piece.possible_moves.append(
                                    (str(new_row), str(new_col), int(x - (diff * i) - diff), int(y - (diff * i) - diff)))
                                piece.root_bishop_moves.append(
                                    [
                                    str(new_row), str(new_col), int(x - (diff * i) - diff), int(y - (diff * i) - diff)])
                            elif self.board[new_row][new_col].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (x - (diff * i) - diff, y - (diff * i) - diff), 20)
                                piece.possible_attacks.append(
                                    (str(new_row), str(new_col), int(x - (diff * i) - diff), int(y - (diff * i) - diff)))
                                piece.root_horse_attacks.append(
                                    [
                                    str(new_row), str(new_col), int(x - (diff * i) - diff), int(y - (diff * i) - diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            # add 100 to x and subtract 100 to y
                            new_row = row + i + 1
                            new_col = column1 - i - 1
                            if new_row > 7 or new_col > 7:
                                break
                            if self.board[new_row][new_col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x + (diff * i) + diff, y - (diff * i) - diff), 20)
                                piece.possible_moves.append(
                                    (str(new_row), str(new_col), int(x + (diff * i) + diff), int(y - (diff * i) - diff)))
                                piece.root_bishop_moves.append(
                                    [
                                    str(new_row), str(new_col), int(x + (diff * i) + diff), int(y - (diff * i) - diff)])
                            elif self.board[new_row][new_col].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (x + (diff * i) + diff, y - (diff * i) - diff), 20)
                                piece.possible_attacks.append(
                                    (str(new_row), str(new_col), int(x + (diff * i) + diff), int(y - (diff * i) - diff)))
                                piece.root_bishop_attacks.append(
                                    [
                                    str(new_row), str(new_col), int(x + (diff * i) + diff), int(y - (diff * i) - diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            # subtract 100 to x and add 100 to y
                            new_row = row - i - 1
                            new_col = column1 + i + 1
                            if new_row > 7 or new_col > 7:
                                break
                            if self.board[new_row][new_col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x - (diff * i) - diff, y + (diff * i) + diff), 20)
                                piece.possible_moves.append(
                                    (str(new_row), str(new_col), int(x - (diff * i) - diff), int(y + (diff * i) + diff)))
                                piece.root_bishop_moves.append(
                                    [
                                    str(new_row), str(new_col), int(x - (diff * i) - diff), int(y + (diff * i) + diff)])
                            elif self.board[new_row][new_col].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (x - (diff * i) - diff, y + (diff * i) + diff), 20)
                                piece.possible_attacks.append(
                                    (str(new_row), str(new_col), int(x - (diff * i) - diff), int(y + (diff * i) + diff)))
                                piece.root_bishop_attacks.append(
                                    [
                                    str(new_row), str(new_col), int(x - (diff * i) - diff), int(y + (diff * i) + diff)])
                                break
                            else:
                                break
                        if len(piece.possible_moves) > 0 or len(piece.possible_attacks) > 0:
                            piece.current.extend([row, column])
                            piece.pressed = True
                elif type_piece == classes[1][3]:
                    print("queenw")
                    if self.turn_color == (255, 255, 255):
                        for i in range(8):
                            # add 100 to y and x
                            new_row = row + i + 1
                            new_col = column1 + i + 1
                            if new_row > 7 or new_col > 7:
                                break
                            if self.board[new_row][new_col].type1 == "none":
                                pygame.draw.circle(win, BLUE, ((x + (diff * i) + diff), y + (diff * i) + diff), 20)
                                piece.possible_moves.append((str(new_row), str(new_col), int(x + (diff * i) + diff), int(y + (diff * i) + diff)))
                                piece.white_root_queen_moves.append([str(new_row), str(new_col), int(x + (diff * i) + diff), int(y + (diff * i) + diff)])
                            elif self.board[new_row][new_col].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, ((x + (diff * i) + diff), y + (diff * i) + diff), 20)
                                piece.possible_attacks.append((str(new_row), str(new_col), int(x + (diff * i) + diff), int(y + (diff * i) + diff)))
                                piece.white_root_queen_attacks.append([str(new_row), str(new_col), int(x + (diff * i) + diff), int(y + (diff * i) + diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            # subtract 100 to y and subtract 100 to x
                            new_row = row - i - 1
                            new_col = column1 - i - 1
                            if new_row > 7 or new_col > 7:
                                break
                            if self.board[new_row][new_col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x - (diff * i) - diff, y - (diff * i) - diff), 20)
                                piece.possible_moves.append((str(new_row), str(new_col), int(x - (diff * i) - diff), int(y - (diff * i) - diff)))
                                piece.white_root_queen_moves.append([str(new_row), str(new_col), int(x - (diff * i) - diff), int(y - (diff * i) - diff)])
                            elif self.board[new_row][new_col].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, (x - (diff * i) - diff, y - (diff * i) - diff), 20)
                                piece.possible_attacks.append((str(new_row), str(new_col), int(x - (diff * i) - diff), int(y - (diff * i) - diff)))
                                piece.white_root_queen_attacks.append([str(new_row), str(new_col), int(x - (diff * i) - diff), int(y - (diff * i) - diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            # add 100 to x and subtract 100 to y
                            new_row = row + i + 1
                            new_col = column1 - i - 1
                            if new_row > 7 or new_col > 7:
                                break
                            if self.board[new_row][new_col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x + (diff * i) + diff, y - (diff * i) - diff), 20)
                                piece.possible_moves.append((str(new_row), str(new_col), int(x + (diff * i) + diff), int(y - (diff * i) - diff)))
                                piece.white_root_queen_moves.append([str(new_row), str(new_col), int(x + (diff * i) + diff), int(y - (diff * i) - diff)])
                            elif self.board[new_row][new_col].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, (x + (diff * i) + diff, y - (diff * i) - diff), 20)
                                piece.possible_attacks.append((str(new_row), str(new_col), int(x + (diff * i) + diff), int(y - (diff * i) - diff)))
                                piece.white_root_queen_attacks.append([str(new_row), str(new_col), int(x + (diff * i) + diff), int(y - (diff * i) - diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            # subtract 100 to x and add 100 to y
                            new_row = row - i - 1
                            new_col = column1 + i + 1
                            if new_row > 7 or new_col > 7:
                                break
                            if self.board[new_row][new_col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x - (diff * i) - diff, y + (diff * i) + diff), 20)
                                piece.possible_moves.append((str(new_row), str(new_col), int(x - (diff * i) - diff), int(y + (diff * i) + diff)))
                                piece.white_root_queen_moves.append([str(new_row), str(new_col), int(x - (diff * i) - diff), int(y + (diff * i) + diff)])
                            elif self.board[new_row][new_col].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, (x - (diff * i) - diff, y + (diff * i) + diff), 20)
                                piece.white_root_queen_attacks.append([str(new_row), str(new_col), int(x - (diff * i) - diff), int(y + (diff * i) + diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            # add 100 to y
                            row = row
                            new_col = column1 + i + 1
                            if row > 7 or new_col > 7:
                                break
                            if self.board[row][new_col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x, y + (diff * i) + diff), 20)
                                piece.possible_moves.append((str(row), str(new_col), int(x), int(y + (diff * i) + diff)))
                                piece.white_root_queen_moves.append([str(row), str(new_col), int(x), int(y + (diff * i) + diff)])
                            elif self.board[row][new_col].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, (x, y + (diff * i) + diff), 20)
                                piece.possible_attacks.append((str(row), str(new_col), int(x), int(y + (diff * i) + diff)))
                                piece.white_root_queen_attacks.append([str(row), str(new_col), int(x), int(y + (diff * i) + diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            # subtract 100 to y
                            row = row
                            new_col = column1 - i - 1
                            if row > 7 or new_col > 7:
                                break
                            if self.board[row][new_col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x, y - (diff * i) - diff), 20)
                                piece.possible_moves.append((str(row), str(new_col), int(x), int(y - (diff * i) - diff)))
                                piece.white_root_queen_moves.append([str(row), str(new_col), int(x), int(y - (diff * i) - diff)])
                            elif self.board[row][new_col].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, (x, y - (diff * i) - diff), 20)
                                piece.possible_attacks.append((str(row), str(new_col), int(x), int(y - (diff * i) - diff)))
                                piece.white_root_queen_attacks.append([str(row), str(new_col), int(x), int(y - (diff * i) - diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            # add 100 to x
                            new_row = row + i + 1
                            col = column1
                            if new_row > 7 or col > 7:
                                break
                            if self.board[new_row][col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x + (diff * i) + diff, y), 20)
                                piece.possible_moves.append((str(new_row), str(col), int(x + (diff * i) + diff), int(y)))
                                piece.white_root_queen_moves.append([str(new_row), str(col), int(x + (diff * i) + diff), int(y)])
                            elif self.board[new_row][col].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, (x + (diff * i) + diff, y), 20)
                                piece.possible_attacks.append((str(new_row), str(col), int(x + (diff * i) + diff), int(y)))
                                piece.white_root_queen_attacks.append([str(new_row), str(col), int(x + (diff * i) + diff), int(y)])
                                break
                            else:
                                break
                        for i in range(8):
                            # subtract 100 to x
                            new_row = row - i - 1
                            col = column1
                            if new_row > 7 or col > 7:
                                break
                            if self.board[new_row][col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x - (diff * i) - diff, y), 20)
                                piece.possible_moves.append((str(new_row), str(col), int(x - (diff * i) - diff), int(y)))
                                piece.white_root_queen_moves.append([str(new_row), str(col), int(x - (diff * i) - diff), int(y)])
                            elif self.board[new_row][col].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, (x - (diff * i) - diff, y), 20)
                                piece.possible_attacks.append((str(new_row), str(col), int(x - (diff * i) - diff), int(y)))
                                piece.white_root_queen_attacks.append([str(new_row), str(col), int(x - (diff * i) - diff), int(y)])
                                break
                            else:
                                break

                        if len(piece.possible_moves) > 0 or len(piece.possible_attacks) > 0:
                            piece.current.extend([row, column])
                            piece.pressed = True
                elif type_piece == classes[0][3]:
                    print("queenb")
                    if self.turn_color == (0, 0, 0):
                        for i in range(8):
                            #add 100 to y and x
                            new_row = row + i + 1
                            new_col = column1 + i + 1
                            if new_row > 7 or new_col > 7:
                                break
                            if self.board[new_row][new_col].type1 == "none":
                                pygame.draw.circle(win, BLUE, ((x + (diff * i) + diff), y + (diff * i) + diff), 20)
                                piece.possible_moves.append((str(new_row), str(new_col), int(x + (diff * i) + diff), int(y +(diff * i) + diff)))
                                piece.root_queen_moves.append([str(new_row), str(new_col), int(x + (diff * i) + diff), int(y +(diff * i) + diff)])
                            elif self.board[new_row][new_col].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, ((x + (diff * i) + diff), y + (diff * i) + diff), 20)
                                piece.possible_attacks.append((str(new_row), str(new_col), int(x + (diff * i) + diff), int(y +(diff * i) + diff)))
                                piece.root_queen_attacks.append([str(new_row), str(new_col), int(x + (diff * i) + diff), int(y +(diff * i) + diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            #subtract 100 to y and subtract 100 to x
                            new_row = row - i - 1
                            new_col = column1 - i - 1
                            if new_row > 7 or new_col > 7:
                                break
                            if self.board[new_row][new_col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x - (diff * i) - diff, y - (diff * i) - diff), 20)
                                piece.possible_moves.append((str(new_row), str(new_col), int(x -(diff * i) - diff), int(y -(diff * i) - diff)))
                                piece.root_queen_moves.append([str(new_row), str(new_col), int(x -(diff * i) - diff), int(y -(diff * i) - diff)])
                            elif self.board[new_row][new_col].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (x - (diff * i) - diff, y - (diff * i) - diff), 20)
                                piece.possible_attacks.append((str(new_row), str(new_col), int(x -(diff * i) - diff), int(y -(diff * i) - diff)))
                                piece.root_queen_attacks.append([str(new_row), str(new_col), int(x -(diff * i) - diff), int(y -(diff * i) - diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            #add 100 to x and subtract 100 to y
                            new_row = row + i + 1
                            new_col = column1 - i - 1
                            if new_row > 7 or new_col > 7:
                                break
                            if self.board[new_row][new_col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x+ (diff * i) + diff, y-(diff * i) - diff), 20)
                                piece.possible_moves.append((str(new_row), str(new_col), int(x+ (diff * i) + diff), int(y-(diff * i) - diff )))
                                piece.root_queen_moves.append([str(new_row), str(new_col), int(x+ (diff * i) + diff), int(y-(diff * i) - diff )])
                            elif self.board[new_row][new_col].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (x+ (diff * i) + diff, y-(diff * i) - diff), 20)
                                piece.possible_attacks.append((str(new_row), str(new_col), int(x+ (diff * i) + diff), int(y-(diff * i) - diff )))
                                piece.root_queen_attacks.append([str(new_row), str(new_col), int(x+ (diff * i) + diff), int(y-(diff * i) - diff )])
                                break
                            else:
                                break
                        for i in range(8):
                            #subtract 100 to x and add 100 to y
                            new_row = row - i - 1
                            new_col = column1 + i + 1
                            if new_row > 7 or new_col > 7:
                                break
                            if self.board[new_row][new_col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x- (diff * i) - diff, y +(diff * i) + diff), 20)
                                piece.possible_moves.append((str(new_row), str(new_col), int(x- (diff * i) - diff), int(y+(diff * i) + diff )))
                                piece.root_queen_moves.append([str(new_row), str(new_col), int(x- (diff * i) - diff), int(y+(diff * i) + diff )])
                            elif self.board[new_row][new_col].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (x- (diff * i) - diff, y +(diff * i) + diff), 20)
                                piece.possible_attacks.append((str(new_row), str(new_col), int(x- (diff * i) - diff), int(y+(diff * i) + diff )))
                                piece.root_queen_attacks.append([str(new_row), str(new_col), int(x- (diff * i) - diff), int(y+(diff * i) + diff )])
                                break
                            else:
                                break
                        for i in range(8):
                            #add 100 to y
                            row = row
                            new_col = column1 + i + 1
                            if row > 7 or new_col > 7:
                                break
                            if self.board[row][new_col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x, y + (diff * i) + diff), 20)
                                piece.possible_moves.append((str(row), str(new_col), int(x), int(y +(diff * i) + diff)))
                                piece.root_queen_moves.append([str(row), str(new_col), int(x), int(y +(diff * i) + diff)])
                            elif self.board[row][new_col].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (x, y + (diff * i) + diff), 20)
                                piece.possible_attacks.append((str(row), str(new_col), int(x), int(y +(diff * i) + diff)))
                                piece.root_queen_attacks.append([str(row), str(new_col), int(x), int(y +(diff * i) + diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            #subtract 100 to y
                            row = row
                            new_col = column1 - i - 1
                            if row > 7 or new_col > 7:
                                break
                            if self.board[row][new_col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x, y - (diff * i) - diff), 20)
                                piece.possible_moves.append((str(row), str(new_col), int(x), int(y -(diff * i) - diff)))
                                piece.root_queen_moves.append([str(row), str(new_col), int(x), int(y -(diff * i) - diff)])
                            elif self.board[row][new_col].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (x, y - (diff * i) - diff), 20)
                                piece.possible_attacks.append((str(row), str(new_col), int(x), int(y -(diff * i) - diff)))
                                piece.root_queen_moves.append([str(row), str(new_col), int(x), int(y -(diff * i) - diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            #add 100 to x
                            new_row = row + i + 1
                            col = column1
                            if new_row > 7 or col > 7:
                                break
                            if self.board[new_row][col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x+ (diff * i) + diff, y ), 20)
                                piece.possible_moves.append((str(new_row), str(col), int(x+ (diff * i) + diff), int(y )))
                                piece.root_queen_moves.append([str(new_row), str(col), int(x+ (diff * i) + diff), int(y )])
                            elif self.board[new_row][col].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (x+ (diff * i) + diff, y ), 20)
                                piece.possible_attacks.append((str(new_row), str(col), int(x+ (diff * i) + diff), int(y )))
                                piece.root_queen_attacks.append([str(new_row), str(col), int(x+ (diff * i) + diff), int(y )])
                                break
                            else:
                                break
                        for i in range(8):
                            #subtract 100 to x
                            new_row = row - i - 1
                            col = column1
                            if new_row > 7 or col > 7:
                                break
                            if self.board[new_row][col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x- (diff * i) - diff, y ), 20)
                                piece.possible_moves.append((str(new_row), str(col), int(x- (diff * i) - diff), int(y )))
                                piece.root_queen_moves.append([str(new_row), str(col), int(x- (diff * i) - diff), int(y )])
                            elif self.board[new_row][col].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (x- (diff * i) - diff, y ), 20)
                                piece.possible_attacks.append((str(new_row), str(col), int(x- (diff * i) - diff), int(y )))
                                piece.root_queen_attacks.append([str(new_row), str(col), int(x- (diff * i) - diff), int(y )])
                                break
                            else:
                                break


                        if len(piece.possible_moves) > 0 or len(piece.possible_attacks) > 0:
                            piece.current.extend([row, column])
                            piece.pressed = True
                elif type_piece == classes[1][4]:
                    print("kingw")
                    if self.turn_color == (255, 255, 255):
                        new_col_same = column
                        new_col_up = column - 1
                        new_col_down = column + 1
                        new_row_same = row
                        new_row_left = row - 1
                        new_row_right = row + 1
                        print(row, new_col_down)
                        if self.board[row][new_col_up].type1 == "none":
                            # up 1
                            pygame.draw.circle(win, BLUE, (x, y - diff), 20)
                            piece.possible_moves.append(((str(row), str(new_col_up), int(x), int(y - diff))))
                            piece.white_root_king_moves.append([str(row), str(new_col_up), int(x), int(y - diff)])
                        elif self.board[row][new_col_up].color == (0, 0, 0):
                            print('y')
                            pygame.draw.circle(win, GREEN, (x, y - diff), 20)
                            piece.possible_attacks.append(((str(row), str(new_col_up), int(x), int(y - diff))))
                            piece.white_root_king_attacks.append([str(row), str(new_col_up), int(x), int(y - diff)])
                        if new_col_down < 0 or new_col_down > 7:
                            pass
                        else:
                            if self.board[row][new_col_down].type1 == "none":
                                # down 1
                                pygame.draw.circle(win, BLUE, (x, y + diff), 20)
                                piece.possible_moves.append(((str(row), str(new_col_down), int(x), int(y + diff))))
                                piece.white_root_king_moves.append([str(row), str(new_col_down), int(x), int(y + diff)])
                            elif self.board[row][new_col_down].color == (0, 0, 0):
                                # down 1
                                pygame.draw.circle(win, GREEN, (x, y + diff), 20)
                                piece.possible_attacks.append(((str(row), str(new_col_down), int(x), int(y + diff))))
                                piece.white_root_king_attacks.append([str(row), str(new_col_down), int(x), int(y + diff)])
                        if new_row_right < 0 or new_row_right > 7:
                            pass
                        else:
                            if self.board[new_row_right][column].type1 == "none":
                                # right 1
                                pygame.draw.circle(win, BLUE, (x + diff, y), 20)
                                piece.possible_moves.append(((str(new_row_right), str(column), int(x + diff), int(y))))
                                piece.white_root_king_moves.append([str(new_row_right), str(column), int(x + diff), int(y)])
                            elif self.board[new_row_right][column].color == (0, 0, 0):
                                # right 1
                                pygame.draw.circle(win, GREEN, (x + diff, y), 20)
                                piece.possible_attacks.append(((str(new_row_right), str(column), int(x + diff), int(y))))
                                piece.white_root_king_attacks.append([str(new_row_right), str(column), int(x + diff), int(y)])
                        if self.board[new_row_left][column].type1 == "none":
                            # left 1
                            pygame.draw.circle(win, BLUE, (x - diff, y), 20)
                            piece.possible_moves.append(((str(new_row_left), str(column), int(x - diff), int(y))))
                            piece.white_root_king_moves.append([str(new_row_left), str(column), int(x - diff), int(y)])
                        elif self.board[new_row_left][column].color == (0, 0, 0):
                            # left 1
                            pygame.draw.circle(win, GREEN, (x - diff, y), 20)
                            piece.possible_attacks.append(((str(new_row_left), str(column), int(x - diff), int(y))))
                            piece.white_root_king_attacks.append([str(new_row_left), str(column), int(x - diff), int(y)])
                        if new_row_right < 0 or new_row_right > 7 or new_col_down < 0 or new_col_down > 7:
                            pass
                        else:
                            if self.board[new_row_right][new_col_down].type1 == "none":
                                # down 1 right 1
                                pygame.draw.circle(win, BLUE, (x + diff, y + diff), 20)
                                piece.possible_moves.append(((str(new_row_right), str(new_col_down), int(x + diff), int(y + diff))))
                                piece.white_root_king_moves.append([str(new_row_right), str(new_col_down), int(x + diff), int(y + diff)])
                            elif self.board[new_row_right][new_col_down].color == (0, 0, 0):
                                # down 1 right 1
                                pygame.draw.circle(win, GREEN, (x + diff, y + diff), 20)
                                piece.possible_attacks.append(((str(new_row_right), str(new_col_down), int(x + diff), int(y + diff))))
                                piece.white_root_king_attacks.append([str(new_row_right), str(new_col_down), int(x + diff), int(y + diff)])
                        if new_row_right < 0 or new_row_right > 7:
                            pass
                        else:
                            if self.board[new_row_right][new_col_up].type1 == "none":
                                # up 1 right 1
                                pygame.draw.circle(win, BLUE, (x + diff, y - diff), 20)
                                piece.possible_moves.append(((str(new_row_right), str(new_col_up), int(x + diff), int(y - diff))))
                                piece.white_root_king_moves.append([str(new_row_right), str(new_col_up), int(x + diff), int(y - diff)])
                            elif self.board[new_row_right][new_col_up].color == (0, 0, 0):
                                # up 1 right 1
                                pygame.draw.circle(win, GREEN, (x + diff, y - diff), 20)
                                piece.possible_attacks.append(((str(new_row_right), str(new_col_up), int(x + diff), int(y - diff))))
                                piece.white_root_king_attacks.append([str(new_row_right), str(new_col_up), int(x + diff), int(y - diff)])
                        if new_col_down > 7 or new_col_down < 0:
                            pass
                        else:
                            if self.board[new_row_left][new_col_down].type1 == "none":
                                # down 1 left 1
                                pygame.draw.circle(win, BLUE, (x - diff, y + diff), 20)
                                piece.possible_moves.append(((str(new_row_left), str(new_col_down), int(x - diff), int(y + diff))))
                                piece.white_root_king_moves.append([str(new_row_left), str(new_col_down), int(x - diff), int(y + diff)])
                            elif self.board[new_row_left][new_col_down].color == (0, 0, 0):
                                # down 1 left 1
                                pygame.draw.circle(win, GREEN, (x - diff, y + diff), 20)
                                piece.possible_attacks.append(((str(new_row_left), str(new_col_down), int(x - diff), int(y + diff))))
                                piece.white_root_king_attacks.append([str(new_row_left), str(new_col_down), int(x - diff), int(y + diff)])
                        if self.board[new_row_left][new_col_up].type1 == "none":
                            # up 1 left 1
                            pygame.draw.circle(win, BLUE, (x - diff, y - diff), 20)
                            piece.possible_moves.append(((str(new_row_left), str(new_col_up), int(x - diff), int(y - diff))))
                            piece.white_root_king_moves.append([str(new_row_left), str(new_col_up), int(x - diff), int(y - diff)])
                        elif self.board[new_row_left][new_col_up].color == (0, 0, 0):
                            # up 1 left 1
                            pygame.draw.circle(win, GREEN, (x - diff, y - diff), 20)
                            piece.possible_attacks.append(((str(new_row_left), str(new_col_up), int(x - diff), int(y - diff))))
                            piece.white_root_king_attacks.append([str(new_row_left), str(new_col_up), int(x - diff), int(y - diff)])

                        if len(piece.possible_moves) > 0 or len(piece.possible_attacks) > 0:
                            piece.current.extend([row, column])
                            piece.pressed = True
                elif type_piece == classes[0][4]:
                    print("kingb")
                    if self.turn_color == (0, 0, 0):
                        new_col_same = column
                        new_col_up = column - 1
                        new_col_down = column +1
                        new_row_same = row
                        new_row_left = row - 1
                        new_row_right = row + 1
                        print(row, new_col_down)
                        if self.board[row][new_col_up].type1 == "none":
                            #up 1
                            pygame.draw.circle(win, BLUE, (x, y-diff), 20)
                            piece.possible_moves.append(((str(row), str(new_col_up), int(x), int(y - diff))))
                            piece.root_king_moves.append([str(row), str(new_col_up), int(x), int(y - diff)])
                        elif self.board[row][new_col_up].color == (255, 255, 255):
                            pygame.draw.circle(win, GREEN, (x, y - diff), 20)
                            piece.possible_attacks.append(((str(row), str(new_col_up), int(x), int(y - diff))))
                            piece.root_king_attacks.append([str(row), str(new_col_up), int(x), int(y - diff)])
                        if new_col_down < 0 or new_col_down > 7:
                            pass
                        else:
                            if self.board[row][new_col_down].type1 == "none":
                                #down 1
                                pygame.draw.circle(win, BLUE, (x, y+diff), 20)
                                piece.possible_moves.append(((str(row), str(new_col_down), int(x), int(y+diff))))
                                piece.root_king_moves.append([str(row), str(new_col_down), int(x), int(y+diff)])
                            elif self.board[row][new_col_down].color == (255, 255, 255):
                                #down 1
                                pygame.draw.circle(win, GREEN, (x, y+diff), 20)
                                piece.possible_attacks.append(((str(row), str(new_col_down), int(x), int(y+diff))))
                                piece.root_king_attacks.append([str(row), str(new_col_down), int(x), int(y+diff)])
                        if new_row_right < 0 or new_row_right > 7 :
                            pass
                        else:
                            if self.board[new_row_right][column].type1 == "none":
                                #right 1
                                pygame.draw.circle(win, BLUE, (x+ diff, y), 20)
                                piece.possible_moves.append(((str(new_row_right), str(column), int(x + diff), int(y))))
                                piece.root_king_moves.append([str(new_row_right), str(column), int(x + diff), int(y)])
                            elif self.board[new_row_right][column].color == (255, 255, 255):
                                #right 1
                                pygame.draw.circle(win, GREEN, (x+ diff, y), 20)
                                piece.possible_attacks.append(((str(new_row_right), str(column), int(x + diff), int(y))))
                                piece.root_king_attacks.append([str(new_row_right), str(column), int(x + diff), int(y)])
                        if self.board[new_row_left][column].type1 == "none":
                            #left 1
                            pygame.draw.circle(win, BLUE, (x - diff, y), 20)
                            piece.possible_moves.append(((str(new_row_left), str(column), int(x - diff), int(y))))
                            piece.root_king_moves.append([str(new_row_left), str(column), int(x - diff), int(y)])
                        elif self.board[new_row_left][column].color == (255, 255, 255):
                            #left 1
                            pygame.draw.circle(win, GREEN, (x - diff, y), 20)
                            piece.possible_attacks.append(((str(new_row_left), str(column), int(x - diff), int(y))))
                            piece.root_king_attacks.append([str(new_row_left), str(column), int(x - diff), int(y)])
                        if new_row_right < 0 or new_row_right > 7 or new_col_down < 0 or new_col_down > 7:
                            pass
                        else:
                            if self.board[new_row_right][new_col_down].type1 == "none":
                                #down 1 right 1
                                pygame.draw.circle(win, BLUE, (x + diff, y+diff), 20)
                                piece.possible_moves.append(((str(new_row_right), str(new_col_down), int(x + diff), int(y+diff))))
                                piece.root_king_moves.append([str(new_row_right), str(new_col_down), int(x + diff), int(y+diff)])
                            elif self.board[new_row_right][new_col_down].color == (255, 255, 255):
                                #down 1 right 1
                                pygame.draw.circle(win, GREEN, (x + diff, y+diff), 20)
                                piece.possible_attacks.append(((str(new_row_right), str(new_col_down), int(x + diff), int(y+diff))))
                                piece.root_king_attacks.append([str(new_row_right), str(new_col_down), int(x + diff), int(y+diff)])
                        if new_row_right < 0 or new_row_right > 7:
                            pass
                        else:
                            if self.board[new_row_right][new_col_up].type1 == "none":
                                #up 1 right 1
                                pygame.draw.circle(win, BLUE, (x + diff, y-diff), 20)
                                piece.possible_moves.append(((str(new_row_right), str(new_col_up), int(x + diff), int(y-diff))))
                                piece.root_king_moves.append([str(new_row_right), str(new_col_up), int(x + diff), int(y-diff)])
                            elif self.board[new_row_right][new_col_up].color == (255, 255, 255):
                                #up 1 right 1
                                pygame.draw.circle(win, GREEN, (x + diff, y-diff), 20)
                                piece.possible_attacks.append(((str(new_row_right), str(new_col_up), int(x + diff), int(y-diff))))
                                piece.root_king_attacks.append([str(new_row_right), str(new_col_up), int(x + diff), int(y-diff)])
                        if new_col_down > 7 or new_col_down < 0:
                            pass
                        else:
                            if self.board[new_row_left][new_col_down].type1 == "none":
                                #down 1 left 1
                                pygame.draw.circle(win, BLUE, (x - diff, y+diff), 20)
                                piece.possible_moves.append(((str(new_row_left), str(new_col_down), int(x - diff), int(y+diff))))
                                piece.root_king_moves.append([str(new_row_left), str(new_col_down), int(x - diff), int(y+diff)])
                            elif self.board[new_row_left][new_col_down].color == (255, 255, 255):
                                #down 1 left 1
                                pygame.draw.circle(win, GREEN, (x - diff, y+diff), 20)
                                piece.possible_attacks.append(((str(new_row_left), str(new_col_down), int(x - diff), int(y+diff))))
                                piece.root_king_attacks.append([str(new_row_left), str(new_col_down), int(x - diff), int(y+diff)])
                        if self.board[new_row_left][new_col_up].type1 == "none":
                            #up 1 left 1
                            pygame.draw.circle(win, BLUE, (x - diff, y-diff), 20)
                            piece.possible_moves.append(((str(new_row_left), str(new_col_up), int(x - diff), int(y-diff))))
                            piece.root_king_moves.append([str(new_row_left), str(new_col_up), int(x - diff), int(y-diff)])
                        elif self.board[new_row_left][new_col_up].color == (255, 255, 255):
                            #up 1 left 1
                            pygame.draw.circle(win, GREEN, (x - diff, y-diff), 20)
                            piece.possible_attacks.append(((str(new_row_left), str(new_col_up), int(x - diff), int(y-diff))))
                            piece.root_king_attacks.append([str(new_row_left), str(new_col_up), int(x - diff), int(y-diff)])

                        if len(piece.possible_moves) > 0 or len(piece.possible_attacks) > 0:
                            piece.current.extend([row, column])
                            piece.pressed = True

                elif type_piece == classes[1][5]:
                    print("pawnw")
                    if self.turn_color == (255, 255, 255):
                        print("dadawdadawda")
                        new_col1 = column1 - 1
                        new_col2 = column1 - 2
                        try:
                            if_first_move = self.board[row][column].first_move
                        except Exception:
                            pass
                        attack_row_right = row + 1
                        attack_row_left = row - 1
                        if row + 1 > 7 or column - 1 < 0 :
                            print("error1")
                        else:
                            if self.board[attack_row_right][new_col1].type1 != "none" and self.board[attack_row_right][new_col1].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, (x + diff, y - diff), 20)
                                piece.possible_attacks.append(((str(attack_row_right), str(new_col1), int(x + diff), int(y - diff))))
                                piece.white_root_pawn_attacks.append([str(attack_row_right), str(new_col1), int(x + diff), int(y - diff)])
                        if row - 1 < 0  or column - 1 < 0:
                            print("error2")

                        else:
                            print(column)
                            if self.board[attack_row_left][new_col1].type1 != "none" and self.board[attack_row_left][
                                new_col1].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, (x - diff, y - diff), 20)
                                piece.possible_attacks.append(((str(attack_row_left), str(new_col1), int(x - diff), int(y - diff))))
                                piece.white_root_pawn_attacks.append([str(attack_row_left), str(new_col1), int(x - diff), int(y - diff)])
                        if column - 1 > 7:
                            pass
                        else:
                            if self.board[row][new_col1].type1 == "none":
                                try:
                                    if if_first_move:
                                        print(x, y)
                                        pygame.draw.circle(win, BLUE, (x ,y - diff), 20)
                                        pygame.draw.circle(win, BLUE, (x ,y - diff*2), 20)
                                        print("dwadawd")
                                        piece.possible_moves.extend(((str(row1), str(new_col1), int(x), int(y-diff)), (str(row1) , str(new_col2), int(x), int(y-diff * 2)),  ))
                                        piece.white_root_pawn_moves.extend([[str(row1), str(new_col1), int(x), int(y-diff)], [str(row1) , str(new_col2), int(x), int(y-diff * 2)], ] )

                                    else:

                                        pygame.draw.circle(win, BLUE, (x, y - diff), 20)
                                        piece.possible_moves.append((str(row1), str(new_col1), int(x), int(y - diff)))
                                        piece.white_root_pawn_moves.append([str(row1), str(new_col1), int(x), int(y - diff)])
                                except Exception:
                                    pass
                            if row == 0:
                                if self.board[row][column - 1].type1 == "none":
                                    print(column)
                                    try:
                                        if if_first_move:
                                            pygame.draw.circle(win, BLUE, (x, y - diff), 20)
                                            pygame.draw.circle(win, BLUE, (x, y - diff * 2), 20)
                                            piece.possible_moves.extend(
                                                [(str(row1), str(new_col1), int(x), int(y - diff)),
                                                 (str(row1), str(new_col2), int(x), int(y - diff * 2)), ])
                                            piece.white_root_pawn_moves.extend(
                                                [[str(row1), str(new_col1), int(x), int(y -diff)],
                                                 [
                                                     str(row1), str(new_col2), int(x), int(y - diff * 2)], ])

                                        else:
                                            pygame.draw.circle(win, BLUE, (x, y - diff), 20)
                                            piece.white_root_pawn_attacks.append(
                                                [str(row1), str(new_col1), int(x), int(y - diff)])
                                            piece.possible_attacks.append(
                                                [str(row1), str(new_col1), int(x), int(y - diff)])
                                    except Exception:
                                        pygame.draw.circle(win, BLUE, (x, y + diff), 20)
                                        piece.white_root_pawn_attacks.append(
                                            [str(row1), str(new_col1), int(x), int(y + diff)])
                        if len(piece.possible_moves) > 0 or len(piece.possible_attacks) > 0:
                            piece.current.extend([row, column])
                            piece.pressed = True
                elif type_piece == classes[0][5]:

                    print("pawnb")
                    if self.turn_color == (0, 0, 0):
                        if_first_move = self.board[row][column].first_move
                        print(if_first_move)
                        new_col1 = column1 + 1
                        new_col2 = column1 + 2

                        attack_row_right = row + 1
                        attack_row_left = row - 1
                        if row + 1 > 7 or column + 1 > 7:
                            pass
                        else:
                            if self.board[attack_row_right][new_col1].type1 != "none" and self.board[attack_row_right][new_col1].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (x + diff, y + diff), 20)
                                piece.possible_attacks.append(((str(attack_row_right), str(new_col1), int(x + diff), int(y + diff))))
                                piece.root_pawn_attacks.append(([str(attack_row_right), str(new_col1), int(x + diff), int(y + diff)]))
                        if row - 1 < 0 or column + 1 > 7:
                            pass
                        else:
                            print(column)
                            if self.board[attack_row_left][new_col1].type1 != "none" and self.board[attack_row_left][new_col1].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (x - diff, y + diff), 20)
                                piece.possible_attacks.append(((str(attack_row_left), str(new_col1), int(x - diff), int(y + diff))))
                                piece.root_pawn_attacks.append(([str(attack_row_left), str(new_col1), int(x - diff), int(y + diff)]))
                        if row - 1 < 0 or column + 1 > 7:
                            pass
                        else:
                            if self.board[row][new_col1].type1 == "none":
                                try:
                                    if if_first_move:
                                        pygame.draw.circle(win, BLUE, (x ,y + diff), 20)
                                        pygame.draw.circle(win, BLUE, (x ,y + diff*2), 20)
                                        piece.possible_moves.extend(((str(row1), str(new_col1), int(x), int(y+diff)), (str(row1) , str(new_col2), int(x), int(y+diff * 2)),  ))
                                        piece.root_pawn_moves.extend([[str(row1), str(new_col1), int(x), int(y+diff)], [str(row1) , str(new_col2), int(x), int(y+diff * 2)],  ])

                                    else:
                                        pygame.draw.circle(win, BLUE, (x, y + diff), 20)
                                        piece.possible_moves.append((str(row1), str(new_col1), int(x), int(y + diff)))
                                        piece.root_pawn_moves.append([str(row1), str(new_col1), int(x), int(y + diff)])
                                except Exception:
                                    pygame.draw.circle(win, BLUE, (x, y + diff), 20)
                                    piece.possible_moves.append((str(row1), str(new_col1), int(x), int(y + diff)))
                                    piece.root_pawn_moves.append([str(row1), str(new_col1), int(x), int(y + diff)])
                        if row == 0:
                            if self.board[row][column + 1].type1 == "none":
                                print(column)
                                try:
                                    if if_first_move:
                                        pygame.draw.circle(win, BLUE, (x, y + diff), 20)
                                        pygame.draw.circle(win, BLUE, (x, y + diff * 2), 20)
                                        piece.possible_moves.extend([(str(row1), str(new_col1), int(x), int(y + diff)),
                                                                     (str(row1), str(new_col2), int(x), int(y + diff * 2)),])
                                        piece.root_pawn_moves.extend([[str(row1), str(new_col1), int(x), int(y + diff)],
                                                                     [
                                                                     str(row1), str(new_col2), int(x), int(y + diff * 2)],])


                                    else:
                                        pygame.draw.circle(win, BLUE, (x, y + diff), 20)
                                        piece.root_pawn_attacks.append([str(row1), str(new_col1), int(x), int(y + diff)])
                                        piece.possible_attacks.append([str(row1), str(new_col1), int(x), int(y + diff)])
                                except Exception:
                                    pygame.draw.circle(win, BLUE, (x, y + diff), 20)
                                    piece.root_pawn_attacks.append([str(row1), str(new_col1), int(x), int(y + diff)])


                        if len(piece.possible_moves) > 0 or len(piece.possible_attacks) > 0:
                            piece.current.extend([row, column])
                            piece.pressed = True
                elif type_piece == classes[1][6] or type_piece == classes[0][6]:
                    print("none")
        else:
            piece.skip = False


    def undo(self,pos, win):

        x1 = pos[0]
        y1 = pos[1]
        win = win
        possible_moves = []
        if len(piece.current) == 2:
            current_row = piece.current[0]
            current_col = piece.current[1]
        else:
            current_row, current_col = "yes", "yes"
        if len(piece.possible_moves) > 0:
            for i in range(len(piece.possible_moves)):
                possible_moves.append([])
                possible = piece.possible_moves[i]
                possible_moves[i].extend([possible[0], possible[1]])




        else:
            current_row, current_col = "2323232", "232332"

        row_press = x1 // SQUARE_SIZE
        col_press = y1 // SQUARE_SIZE


        if piece.pressed:
            global erase_all
            global ready
            erase_all= False
            ready = False
            loop_over = False
            print("pressed")

            if row_press == current_row and current_col == col_press:
                # if user clicks on the piece again it deletes the blue circles

                for i in range(len(piece.possible_moves)):
                    num1 = piece.possible_moves[i][0]
                    num2 = piece.possible_moves[i][1]
                    if num1 in odd1:
                        if num2 in odd1:
                            #red square

                            pygame.draw.rect(win, RED, (piece.possible_moves[i][2] - 50, piece.possible_moves[i][3] - 50, 100, 100))
                            print("r")
                        else:
                            #print("b")
                            #black square
                            pygame.draw.rect(win, BLACK, (piece.possible_moves[i][2] - 50, piece.possible_moves[i][3] - 50, 100, 100))
                    elif num1 in even1:

                        if num2 in even1:
                            print("r")
                            #red square

                            pygame.draw.rect(win, RED, (piece.possible_moves[i][2] - 50, piece.possible_moves[i][3] - 50, 100 ,100))

                        else:
                            print("b")
                            #black square
                            pygame.draw.rect(win, BLACK, (piece.possible_moves[i][2] - 50, piece.possible_moves[i][3] - 50, 100 ,100))

                for i in range(len(piece.possible_attacks)):
                    num1 = piece.possible_attacks[i][0]
                    num2 = piece.possible_attacks[i][1]
                    if num1 in odd1:
                        if num2 in odd1:
                            #red square

                            pygame.draw.rect(win, RED, (piece.possible_attacks[i][2] - 50, piece.possible_attacks[i][3] - 50, 100, 100))
                            print("r")
                        else:
                            #print("b")
                            #black square
                            pygame.draw.rect(win, BLACK, (piece.possible_attacks[i][2] - 50, piece.possible_attacks[i][3] - 50, 100, 100))
                    elif num1 in even1:

                        if num2 in even1:
                            print("r")
                            #red square

                            pygame.draw.rect(win, RED, (piece.possible_attacks[i][2] - 50, piece.possible_attacks[i][3] - 50, 100 ,100))

                        else:
                            print("b")
                            #black square
                            pygame.draw.rect(win, BLACK, (piece.possible_attacks[i][2] - 50, piece.possible_attacks[i][3] - 50, 100 ,100))

                    piece_draw = self.board[int(num1)][int(num2)]
                    piece_draw.draw(win)


                piece.possible_moves.clear()
                piece.possible_attacks.clear()

                piece.current.remove(piece.current[0])
                piece.current.remove(piece.current[0])
                piece.pressed = False
                piece.skip = True

            for i in range(len(piece.possible_moves)):

                num1 = piece.possible_moves[i][0]
                num2 = piece.possible_moves[i][1]

                if str(row_press) == num1 and str(col_press) == num2:
                    erase_all = True
                    loop_over = True

                    break
            for i in range(len(piece.possible_attacks)):
                num1 = piece.possible_attacks[i][0]
                num2 = piece.possible_attacks[i][1]
                if str(row_press) == num1 and str(col_press) == num2:
                    erase_all = True
                    loop_over = True
                    break

                    # if user presses on one of the possible moves
            if loop_over:
                def erase():
                    for i in range(len(piece.possible_moves)):
                        num1 = piece.possible_moves[i][0]
                        num2 = piece.possible_moves[i][1]
                        #removes circles if you move
                        if num1 in odd1:
                            if num2 in odd1:
                                # red square
                                pygame.draw.circle(win, RED, (piece.possible_moves[i][2], piece.possible_moves[i][3]),20)
                                # print("r")
                            else:
                                # print("b")
                                # black square
                                pygame.draw.circle(win, BLACK, (piece.possible_moves[i][2], piece.possible_moves[i][3]),20)
                        elif num1 in even1:
                            if num2 in even1:
                                # print("r")
                                # red square
                                pygame.draw.circle(win, RED, (piece.possible_moves[i][2], piece.possible_moves[i][3]),
                                                   20)
                            else:
                                # print("b")
                                # black square
                                pygame.draw.circle(win, BLACK, (piece.possible_moves[i][2], piece.possible_moves[i][3]),
                                                   20)

                    for i in range(len(piece.possible_attacks)):
                        print("ddddddddddddd")
                        print(i)
                        print("ddddddddddddd")

                        num1 = piece.possible_attacks[i][0]
                        num2 = piece.possible_attacks[i][1]
                        if num1 in odd1:
                            if num2 in odd1:
                                # red square

                                pygame.draw.rect(win, RED, (
                                piece.possible_attacks[i][2] - 50, piece.possible_attacks[i][3] - 50, 100, 100))
                                print("r")
                            else:
                                # print("b")
                                # black square
                                pygame.draw.rect(win, BLACK, (
                                piece.possible_attacks[i][2] - 50, piece.possible_attacks[i][3] - 50, 100, 100))
                        elif num1 in even1:

                            if num2 in even1:
                                print("r")
                                # red square

                                pygame.draw.rect(win, RED, (
                                piece.possible_attacks[i][2] - 50, piece.possible_attacks[i][3] - 50, 100, 100))

                            else:
                                print("b")
                                # black square
                                pygame.draw.rect(win, BLACK, (
                                piece.possible_attacks[i][2] - 50, piece.possible_attacks[i][3] - 50, 100, 100))

                        piece_draw = self.board[int(num1)][int(num2)]
                        piece_draw.draw(win)
                        try:
                            if int(num1) == int(row_press) and int(num2) == int(col_press):
                                if self.board[int(num1)][int(num2)].color == (255, 255, 255):
                                    print("killed white")
                                    el = str((self.board[int(row_press)][int(col_press)].type1))
                                    piece.white_alive.remove(" " + el)
                                    piece.white_dead.append(self.board[int(num1)][int(num2)])
                                else:
                                    print("killed black")
                                    print(piece.black_alive)
                                    el = str((self.board[int(row_press)][int(col_press)].type1))
                                    print(" " + el)
                                    piece.black_alive.remove(el)
                                    piece.black_dead.append(self.board[int(num1)][int(num2)])
                        except Exception:
                            pass


                    #pygame.draw.circle(win, WHITE, ((row_press * SQUARE_SIZE+50), (col_press * SQUARE_SIZE+50)), 20)
                    a = (piece.current[0])
                    b = (piece.current[1])
                    typea = self.board[a][b].type1
                    colora = self.board[a][b].color
                    print("-------------------------------------")
                    #print(self.board[row_press][col_press].type1)
                    self.board[row_press].pop(col_press)

                    self.board[row_press].insert(col_press,(piece(colora, row_press, col_press, typea)))
                    print("-----------------------------------------")
                    piece_draw = self.board[row_press][col_press]
                    if str(row_press) in odd1:
                        if str(col_press) in odd1:
                            # red square

                            pygame.draw.rect(win, RED, (row_press * SQUARE_SIZE ,col_press * SQUARE_SIZE , 100, 100))
                            print("r")
                        else:
                            # print("b")
                            # black square
                            pygame.draw.rect(win, BLACK, (row_press * SQUARE_SIZE , col_press * SQUARE_SIZE , 100, 100))
                    elif str(row_press) in even1:
                        if str(col_press) in even1:
                            print("r")
                            # red square

                            pygame.draw.rect(win, RED, (
                                row_press *SQUARE_SIZE , col_press * SQUARE_SIZE , 100, 100))

                        else:
                            print("b")
                            # black square
                            pygame.draw.rect(win, BLACK, (
                                row_press * SQUARE_SIZE ,col_press * SQUARE_SIZE , 100, 100))
                    piece_draw.draw(win)
            if erase_all:
                erase()
                ready = True

            if ready:
                a = (piece.current[0])
                b = (piece.current[1])
                piece.possible_moves.clear()
                piece.possible_attacks.clear()

                print("yoshu")
                if str(a) in odd1:
                    print(a, b)
                    if str(b) in odd1:
                        # red square
                        c = RED
                        pygame.draw.rect(WIN, c, (a*SQUARE_SIZE, b*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                        print("red")
                    elif str(b) in even1:
                        # black square
                        c = BLACK
                        print("black")
                        pygame.draw.rect(WIN, c, (a*SQUARE_SIZE, b*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                elif str(a) in even1:
                    if str(b) in even1:
                        # red square
                        c = RED
                        pygame.draw.rect(WIN, c, (a*SQUARE_SIZE, b*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                    else:
                        # black square
                        c = BLACK
                        pygame.draw.rect(WIN, c, (a*SQUARE_SIZE, b*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

                if self.board[a][b].type1 == "pawnb" or self.board[a][b].type1 == "pawnw":
                    self.board[row_press][col_press].first_move = False

                self.board[a].pop(b)
                self.board[a].insert(b, ((piece(GREY, a, b, "none"))))

                piece.current.remove(piece.current[0])
                piece.current.remove(piece.current[0])
                piece.pressed = False
                piece.skip = True
                self.turn += 1
                if self.turn_color == (0,0, 0):
                    print("black turn over")
                    self.turn_color = (255, 255, 255)
                    self.turn_over = True
                else:
                    print("white turn over")
                    self.turn_color = (0, 0, 0)
                    self.turn_over = True



            if len(piece.possible_moves) == 0 and len(piece.possible_attacks) > 0 and row_press != current_row and current_col != col_press:
                #if user clicks on a different spot and there is only attacks on screen
                for i in range(len(piece.possible_attacks)):
                    num1 = piece.possible_attacks[i][0]
                    num2 = piece.possible_attacks[i][1]
                    if num1 in odd1:
                        if num2 in odd1:
                            # red square

                            pygame.draw.rect(win, RED, (
                                piece.possible_attacks[i][2] - 50, piece.possible_attacks[i][3] - 50, 100, 100))
                            print("r")
                        else:
                            # print("b")
                            # black square
                            pygame.draw.rect(win, BLACK, (
                                piece.possible_attacks[i][2] - 50, piece.possible_attacks[i][3] - 50, 100, 100))
                    elif num1 in even1:

                        if num2 in even1:
                            print("r")
                            # red square

                            pygame.draw.rect(win, RED, (
                                piece.possible_attacks[i][2] - 50, piece.possible_attacks[i][3] - 50, 100, 100))

                        else:
                            print("b")
                            # black square
                            pygame.draw.rect(win, BLACK, (
                                piece.possible_attacks[i][2] - 50, piece.possible_attacks[i][3] - 50, 100, 100))

                    piece_draw = self.board[int(num1)][int(num2)]
                    piece_draw.draw(win)
                    
                piece.current.clear()
                piece.possible_attacks.clear()
                piece.pressed = False
    def win(self, win):
        for i in str(len(piece.white_dead)):
            if len(piece.white_dead) != 0:
                if piece.white_dead[int(i) - 1].type1 == "kingw":
                    print("victory for black")
                    win.fill(WHITE)
                    pygame.font.init()
                    myfont = pygame.font.SysFont('Comic Sans MS', 93)
                    textsurface = myfont.render('Victory For Black', False, GREEN)
                    win.blit(textsurface, (0, 200))
                    pygame.display.update()
                    time.sleep(7)
                    pygame.quit()

        for i in str(len(piece.black_dead)):
            print(i)
            if len(piece.black_dead) != 0:
                if piece.black_dead[int(i) - 1].type1 == "kingb":
                    print("victory for white")
                    win.fill(WHITE)
                    pygame.font.init()
                    myfont = pygame.font.SysFont('Comic Sans MS', 93)
                    textsurface = myfont.render('Victory For White', False, GREEN)
                    win.blit(textsurface, (0, 200))
                    pygame.display.update()
                    time.sleep(7)
                    pygame.quit()
    def AI(self, win):
        #solved problem that copy would affect other copies with deepcopy
        self.board_temp = copy.deepcopy(self.board)
        for row in range(8):
            for col in range(8):
                if self.board_temp[row][col].type1 == "none":
                    self.board_temp[row][col].color = (0,0,0)
                    self.board_temp[row][col].type1 = "pawnb"

        self.b_move_attack = []
        self.w_move_attack = []
        self.pawns = []
        self.white_pawns = []
        self.horses = []
        self.white_horses = []
        self.queen = []
        self.white_queen = []
        self.king = []
        self.white_king = []
        self.rooks = []
        self.white_rooks = []
        self.bishops = []
        self.white_bishops = []
        self.pawnb_num = 0
        self.horseb_num = 0
        self.queenb_num = 0
        self.kingb_num = 0
        self.rookb_num = 0
        self.bishopb_num = 0
        self.pawnw_num = 0
        self.horsew_num = 0
        self.queenw_num = 0
        self.kingw_num = 0
        self.rookw_num = 0
        self.bishopw_num = 0

        pawnw_num = 0
        horsew_num = 0
        queenw_num = 0
        kingw_num = 0
        rookw_num = 0
        bishopw_num = 0
        if self.turn_color == (0, 0, 0):
            for row in range(8):
                for col in range(8):
                    type2 = self.board[row][col].type1
                    color = self.board[row][col].color
                    if self.board[row][col].color == (0,0,0):
                        piece.skip = False
                        piece.pressed = False
                        self.setup(type2, row, col, color,self.turn, win)
                        if type2 == "pawnb":
                            self.pawnb_num += 1
                            self.pawns.append([(f"pawnb{self.pawnb_num}"),piece.root_pawn_moves, piece.root_pawn_attacks, row ,col])
                            piece.root_pawn_moves = []
                            piece.root_pawn_attacks = []
                        if type2 == "horseb":
                            self.horseb_num += 1
                            self.horses.append([(f"horseb{self.horseb_num}"),piece.root_horse_moves, piece.root_horse_attacks, row ,col])
                            piece.root_horse_moves = []
                            piece.root_horse_attacks = []
                        if type2 == "bishopb":
                            self.bishopb_num += 1
                            self.bishops.append([(f"bishopb{self.bishopb_num}"), piece.root_bishop_moves, piece.root_bishop_attacks, row ,col])
                            piece.root_bishop_moves = []
                            piece.root_bishop_attacks = []
                        if type2 == "rookb":
                            self.rookb_num += 1
                            self.rooks.append([(f"rookb{self.rookb_num}"), piece.root_rook_moves, piece.root_rook_attacks, row ,col])
                            piece.root_rook_moves = []
                            piece.root_rook_attacks = []
                        if type2 == "queenb":
                            self.queenb_num += 1
                            self.queen.append([(f"queenb{self.queenb_num}"), piece.root_queen_moves, piece.root_queen_attacks, row ,col])
                            piece.root_queen_moves = []
                            piece.root_queen_attacks = []
                        if type2 == "kingb":
                            self.kingb_num += 1
                            self.king.append([(f"kingb{self.kingb_num}"), piece.root_king_moves, piece.root_king_attacks, row ,col])
                            piece.root_king_moves = []
                            piece.root_king_attacks = []

            for row in range(8):
                for col in range(8):
                    type2 = self.board[row][col].type1
                    color = self.board[row][col].color
                    if self.board[row][col].color == (255,255,255):
                        piece.skip = False
                        piece.pressed = False
                        self.turn_color = (255, 255, 255)
                        ai.setup1(self, type2, row, col, color,self.turn, win)
                        if type2 == "pawnw":
                            self.pawnw_num += 1
                            self.white_pawns.append([(f"pawnw{self.pawnw_num}"),piece.white_root_pawn_moves, piece.white_root_pawn_attacks])
                            piece.white_root_pawn_moves = []
                            piece.white_root_pawn_attacks = []
                        if type2 == "horsew":
                            self.horsew_num += 1
                            self.white_horses.append([(f"horsew{self.horsew_num}"),piece.white_root_horse_moves, piece.white_root_pawn_attacks])
                            piece.white_root_horse_moves = []
                            piece.white_root_horse_attacks = []
                        if type2 == "bishopw":
                            self.bishopw_num += 1
                            self.white_bishops.append([(f"bishopw{self.bishopw_num}"), piece.white_root_bishop_moves, piece.white_root_bishop_attacks])
                            piece.white_root_bishop_moves = []
                            piece.white_root_bishop_attacks = []
                        if type2 == "rookw":
                            self.rookw_num += 1
                            self.white_rooks.append([(f"rookw{self.rookw_num}"), piece.white_root_rook_moves, piece.white_root_rook_attacks])
                            piece.white_root_rook_moves = []
                            piece.white_root_rook_attacks = []
                        if type2 == "queenw":
                            self.queenw_num += 1
                            self.white_queen.append([(f"queenw{self.queenw_num}"), piece.white_root_queen_moves, piece.white_root_queen_attacks])
                            piece.white_root_queen_moves = []
                            piece.white_root_queen_attacks = []
                        if type2 == "kingw":
                            self.kingw_num += 1
                            self.white_king.append([(f"kingw{self.kingw_num}"), piece.white_root_king_moves, piece.white_root_king_attacks])
                            piece.white_root_king_moves = []
                            piece.white_root_king_attacks = []

            self.b_move_attack.extend([[self.pawns], [self.rooks], [self.bishops], [self.horses], [self.queen], [self.king]])
            self.w_move_attack.extend([[self.white_pawns], [self.white_rooks], [self.white_bishops], [self.white_horses], [self.white_queen], [self.white_king]])

            self.delle()
            piece.possible_attacks.clear()
            self.get_val(win)
            self.ai_move(win)

            piece.current.clear()
            piece.possible_attacks.clear()
            piece.possible_moves.clear()
            self.turn_over = False
            self.turn_color = (255,255,255)
            piece.skip = False
            piece.pressed = False
            self.del2()
            self.er(win)
    def ai_move(self, win):
        rank = self.board[self.best_move[0][0][0]][self.best_move[0][0][1]].type1

        ra = ""
        for let in rank:
            if let.isnumeric():
                pass
            else:
                ra += let
        if rank == "kingw":
            print("DEFEAT")
            win.fill(WHITE)
            pygame.font.init()
            myfont = pygame.font.SysFont('Comic Sans MS', 120)
            textsurface = myfont.render('DEFEAT', False, GREEN)
            win.blit(textsurface, (0, 200))
            pygame.display.update()
            time.sleep(7)
            pygame.quit()
        print(self.best_move[0])
        self.board[self.best_move[0][2]].pop(self.best_move[0][3])
        self.board[self.best_move[0][2]].insert(self.best_move[0][3], (piece((0, 0, 0), self.best_move[0][2], self.best_move[0][3], "none")))

        x = int(int(self.best_move[0][0][0]) * SQUARE_SIZE )
        y = int(int(self.best_move[0][0][1]) * SQUARE_SIZE)

        rank = str((self.best_move[0][1]))
        ra = ""
        for let in rank:
            if let.isnumeric():
                pass
            else:
                ra += let
        if ra == classes[0][5]:
            print("pawn")
            win.blit(pawnb, (x - 50, y))
        elif ra == classes[0][1]:
            win.blit(horseb, (x, y))
            print("horse")
        elif ra == classes[0][0]:
            # print("rook")
            win.blit(rookb, (x - 55, y - 25))
            pass

        elif ra == classes[0][1]:
            win.blit(horseb, (x, y))
            # print("horse")
        elif ra == classes[0][2]:
            # print("bishop")
            win.blit(bishopb, (x - 15, y))

        elif ra == classes[0][3]:
            win.blit(queenb, (x - 70,y - 34))
            # print("queen")
        elif ra == classes[0][4]:
            # print("king")
            win.blit(kingb, (x - 60, y - 13))
        x = int(self.best_move[0][0][0])
        y = int(self.best_move[0][0][1])
        self.board[x].pop(y)
        self.board[x].insert(y, (piece((0, 0, 0), x, y, ra)))
        rank1 = (self.best_move[0][1])
        ra1 = ""
        for let in rank1:
            if let.isnumeric():
                pass
            else:
                ra1 += let
        if ra1 == "pawnb":
            print(self.best_move)
            print(self.best_move[0][0][0], self.best_move[0][0][1])
            # time.sleep(3)
            self.board[self.best_move[0][0][0]][self.best_move[0][0][1]].first_move = False
    def w_attack(self):
        self.all_white_attacks = []
        w_ran = len(self.w_move_attack)
        for i in range(w_ran):
            w_classes = len((self.w_move_attack[i]))
            for c in range(w_classes):
                w_extra = len(self.w_move_attack[i][c])

                for d in range(w_extra):

                    w_moves = len((self.w_move_attack[i][c][d][1]))
                    w_attacks = len((self.w_move_attack[i][c][d][2]))

                    print(w_moves)
                    for a in range(w_moves):

                        # moves
                        w_move = (self.w_move_attack[i][c][d][1][a])

                        if str(self.w_move_attack[i][c][d][0]) == "queenw1" or str(self.w_move_attack[i][c][d][0]) == "bishopw1" or str(self.w_move_attack[i][c][d][0]) == "rookw1" or str(self.w_move_attack[i][c][d][0]) == "bishopw2" or str(self.w_move_attack[i][c][d][0]) == "rookw2":
                            self.all_white_attacks.append([w_move])

                    for b in range(w_attacks):
                        # attacks
                        w_attack = self.w_move_attack[i][c][d][2][b]

                        self.all_white_attacks.append([w_attack])
    def get_val(self, win):
        self.w_attack()
        self.delle()
        for i in range(len(self.all_white_attacks)):

            x = int((self.all_white_attacks[i][0][0]))
            y = int((self.all_white_attacks[i][0][1]))
            if self.board[x][y].type1 == "kingb":
                print("Check")
                self.check = True

        ran = len(self.b_move_attack)
        for i in range(ran):
            classes = len((self.b_move_attack[i]))
            for c in range(classes):
                extra = len(self.b_move_attack[i][c])

                for d in range(extra):
                    moves = len((self.b_move_attack[i][c][d][1]))
                    attacks = len((self.b_move_attack[i][c][d][2]))
                    for a in range(moves):
                        # moves
                        move = (self.b_move_attack[i][c][d][1][a])
                        point = 0
                        self.b_move_attack[i][c][d][1][a].append(point)


                        if int(move[1]) >=4:
                            point += 2
                        # if int(move)
                        self.turn_color = (0,0,0)
                        self.board_temp1 = copy.deepcopy(self.board)
                        for row in range(8):
                            for col in range(8):
                                pass

                        rank = str(self.b_move_attack[i][c][d][0])
                        ra = ""
                        for let in rank:
                            if let.isnumeric():
                                pass
                            else:
                                ra += let
                        piece.skip = False
                        piece.pressed = False
                        w_xy2 = 0
                        ai.setup1(self, ra, int(move[0]), int(move[1]), (0,0,0), self.turn, win)
                        for row in range(8):
                            for col in range(8):
                                if self.board[row][col].type1 == "kingw":
                                    w_xy2 = str(row) + str(col)


                        if len(piece.black_attacks) != 0:
                            for ia in range(len(piece.black_attacks)):
                                b_xy2 = piece.black_attacks[ia][0] + piece.black_attacks[ia][1]
                                print(piece.black_attacks)
                                if b_xy2 == w_xy2:
                                    point += 99999999999999999999999999999


                        if len(self.all_white_attacks) != 0:
                            for o in range(len(self.all_white_attacks)):
                                w_xy = str(self.all_white_attacks[o][0][0]) + str(self.all_white_attacks[o][0][1])
                                b_xy = str(move[0]) + str(move[1])
                                name = (self.b_move_attack[i][c][d][0])
                                rank230 = ""
                                for let in range(len(name)):
                                    if name[let].isdigit():
                                        print("true")
                                    else:
                                        rank230 += name[let]

                                if w_xy == b_xy:
                                    if rank230 == "pawnb":
                                        point -= 3
                                    if rank230 == "rookb":
                                        point -= 5
                                    if rank230 == "bishopb":
                                        point -= 5
                                    if rank230 == "horseb":
                                        point -= 6
                                    if rank230 == "queenb":
                                        point -= 13
                                    # if rank230 == "kingb":
                                    #     point -= 99999999999999999999999999999999999999

                        name = (self.b_move_attack[i][c][d][0])
                        rank230 = ""
                        for let in range(len(name)):
                            if name[let].isdigit():
                                print("true")
                            else:
                                rank230 += name[let]
                        if rank230 == "kingb" and self.check:
                            if point >= 0:
                                point += 999999999999999999999999999999999999999999999999999999999999999999999999

                        self.b_move_attack[i][c][d][1][a].append(point)
                        piece.black_attacks.clear()
                        point = 0
                    for b in range(attacks):
                        # attacks
                        point = 0
                        attack = self.b_move_attack[i][c][d][2][b]
                        if len(self.all_white_attacks) != 0:
                            for o in range(len(self.all_white_attacks)):
                                w_xy = str(self.all_white_attacks[o][0][0]) + str(self.all_white_attacks[o][0][1])
                                b_xy = str(attack[0]) + str(attack[1])
                                name = (self.b_move_attack[i][c][d][0])
                                rank230 = ""
                                for let in range(len(name)):
                                    if name[let].isdigit():
                                        print("true")
                                    else:
                                        rank230 += name[let]

                                if w_xy == b_xy:
                                    if rank230 == "pawnb":
                                        point -= 3
                                    if rank230 == "rookb":
                                        point -= 5
                                    if rank230 == "bishopb":
                                        point -= 5
                                    if rank230 == "horseb":
                                        point -= 6
                                    if rank230 == "queenb":
                                        point -= 13
                                    # if rank230 == "kingb":
                                    #     point -= 99999999999999999999999999999999999999
                        if self.board[int(attack[0])][int(attack[1])].type1 == "pawnw":
                            point += 3
                        if self.board[int(attack[0])][int(attack[1])].type1 == "rookw":
                            point += 5
                        if self.board[int(attack[0])][int(attack[1])].type1 == "bishopw":
                            point += 5
                        if self.board[int(attack[0])][int(attack[1])].type1 == "queenw":
                            point += 13
                        if self.board[int(attack[0])][int(attack[1])].type1 == "kingw":
                            point += 99999999999999999999999999999999999999999999

                        rank = str(self.b_move_attack[i][c][d][0])
                        ra = ""
                        for let in rank:
                            if let.isnumeric():
                                pass
                            else:
                                ra += let
                        piece.skip = False
                        piece.pressed = False
                        w_xy2 = 0
                        ai.setup1(self, ra, int(attack[0]), int(attack[1]), (0, 0, 0), self.turn, win)
                        for row in range(8):
                            for col in range(8):
                                if self.board[row][col].type1 == "kingw":
                                    w_xy2 = str(row) + str(col)
                        if len(piece.black_attacks) != 0:
                            for ia in range(len(piece.black_attacks)):
                                b_xy2 = piece.black_attacks[ia][0] + piece.black_attacks[ia][1]
                                print(piece.black_attacks)
                                if b_xy2 == w_xy2:
                                    point += 99999999999999999999999999999
                        name = (self.b_move_attack[i][c][d][0])
                        rank230 = ""
                        for let in range(len(name)):
                            if name[let].isdigit():
                                print("true")
                            else:
                                rank230 += name[let]
                        if rank230 == "kingb" and self.check:
                            if point >= 0:
                                point += 999999999999999999999999999999999999999999999999999999999999999999999999
                        self.b_move_attack[i][c][d][2][b].append(point)
                        point = 0
        print(self.b_move_attack)
        self.best_move = [[[0,0], [0,0], [0,0], 0, -9999999999999999999999999]]
        unorganized = []
        ran = len(self.b_move_attack)
        for i in range(ran):
            classes = len((self.b_move_attack[i]))
            for c in range(classes):
                extra = len(self.b_move_attack[i][c])

                for d in range(extra):
                    moves = len((self.b_move_attack[i][c][d][1]))
                    attacks = len((self.b_move_attack[i][c][d][2]))
                    rank = str(self.b_move_attack[i][c][d][0])
                    for a in range(moves):
                        # moves
                        move = (self.b_move_attack[i][c][d][1][a])
                        unorganized.append([move,rank, self.b_move_attack[i][c][d][3],self.b_move_attack[i][c][d][4] ])

                        # if move[4] > piece.best_move[4]:
                        #     self.best_move.clear()
                        #     self.best_move.append([move, self.b_move_attack[i][c][d][3], self.b_move_attack[i][c][d][4]])
                        # elif move[4] == piece.best_move[4]:
                        #     if a == ra:
                        #         self.best_move.clear()
                        #         self.best_move.append([move, self.b_move_attack[i][c][d][3], self.b_move_attack[i][c][d][4],self.b_move_attack[i][c][d][0] ])

                    for b in range(attacks):
                        # attacks
                        attack = self.b_move_attack[i][c][d][2][b]

                        if len(attack) == 5:
                            attack.insert(3, 0)
                        unorganized.append([attack,rank, self.b_move_attack[i][c][d][3],self.b_move_attack[i][c][d][4] ])

        numb = (len(unorganized))
        random_number = random.randint(1, numb)
        for i in range(numb):
            if unorganized[i][0][5] > self.best_move[0][4]:
                self.best_move.clear()
                self.best_move.append([[int(unorganized[i][0][0]), int(unorganized[i][0][1]) ], unorganized[i][1], unorganized[i][2], unorganized[i][3],unorganized[i][0][5]] )
            elif i == random_number and unorganized[i][0][5] == self.best_move[0][4]:
                self.best_move.clear()
                self.best_move.append([[int(unorganized[i][0][0]), int(unorganized[i][0][1])], unorganized[i][1], unorganized[i][2], unorganized[i][3],unorganized[i][0][5]])

    def delle(self):
        ran = len((self.b_move_attack))


        for i in range(ran):
            classes = len((self.b_move_attack[i]))
            for c in range(classes):
                extra = len(self.b_move_attack[i][c])
                for d in range(extra):
                    moves = len((self.b_move_attack[i][c][d][1]))
                    attacks = len((self.b_move_attack[i][c][d][2]))

                    for a in range(moves):
                        # moves
                        try:
                            move = self.b_move_attack[i][c][d][1][a]
                        except Exception:
                            a = - 1
                            try:
                                move = self.b_move_attack[i][c][d][1][a]
                            except Exception:
                                a = - 1
                                move = self.b_move_attack[i][c][d][1][a]
                                pass

                        if int(move[0]) < 0 or int(move[0]) > 7:
                            self.b_move_attack[i][c][d][1].pop(a)
                        elif int(move[1]) < 0 or int(move[1]) > 7:
                            self.b_move_attack[i][c][d][1].pop(a)
                    for b in range(attacks):
                        # attacks
                        try:
                            attack = self.b_move_attack[i][c][d][2][b]
                        except Exception:
                            b =- 1
                            try:
                                attack = self.b_move_attack[i][c][d][2][b]
                            except Exception:
                                b = - 1
                                attack = self.b_move_attack[i][c][d][2][b]
                                pass
                     
                        #print(attack[1])
                        if int(attack[0]) < 0 or int(attack[0]) > 7:
                            self.b_move_attack[i][c][d][2].pop(b)
                            #print("WORKED")
                        elif int(attack[1]) < 0 or int(attack[1]) > 7:
                            self.b_move_attack[i][c][d][2].pop(b)
                            #print("WORKED")
        ran = len((self.all_white_attacks))
        if ran != 0:
            t = 0
            for i in range(ran):
                #print(self.all_white_attacks[i - t])
                a = self.all_white_attacks[i - t][0][0]
                b = self.all_white_attacks[i - t][0][1]
                if int(a) >7 or int(a) < 0:
                    self.all_white_attacks.pop(i - t)
                    t += 1

                elif int(b) >7 or int(b) < 0:
                    self.all_white_attacks.pop(i - t)
                    t += 1






    def er(self, win):
        for row in range(8):
            for col in range(8):
                if row % 2 == 1 :
                    if col % 2 == 1:
                        # red square

                        pygame.draw.rect(win, RED,
                                         (row * SQUARE_SIZE , col * SQUARE_SIZE , 100, 100))
                        #print("r")
                    else:
                        # print("b")
                        # black square
                        pygame.draw.rect(win, BLACK,
                                         (row * SQUARE_SIZE , col * SQUARE_SIZE , 100, 100))
                elif row % 2 == 0:

                    if col% 2 == 0:
                        #print("r")
                        # red square

                        pygame.draw.rect(win, RED,
                                         (row * SQUARE_SIZE , col * SQUARE_SIZE , 100, 100))

                    else:
                        #print("b")
                        # black square
                        pygame.draw.rect(win, BLACK,
                                         (row * SQUARE_SIZE , col * SQUARE_SIZE , 100, 100))
        for row in range(8):
            for col in range(8):
                piece_draw = self.board[row][col]
                piece_draw.draw(win)


    def del2(self):
            self.board_temp.clear()
            piece.root_pawn_attacks.clear()
            piece.root_pawn_moves.clear()
            self.all_white_attacks.clear()
            piece.root_king_attacks.clear()
            piece.root_king_moves.clear()

            piece.root_queen_attacks.clear()
            piece.root_queen_moves.clear()

            piece.root_horse_attacks.clear()
            piece.root_horse_moves.clear()

            piece.root_bishop_attacks.clear()
            piece.root_bishop_moves.clear()

            piece.root_rook_attacks.clear()
            piece.root_rook_moves.clear()

            piece.white_root_pawn_attacks.clear()
            piece.white_root_pawn_moves.clear()

            piece.white_root_king_attacks.clear()
            piece.white_root_king_moves.clear()

            piece.white_root_queen_attacks.clear()
            piece.white_root_queen_moves.clear()

            piece.white_root_horse_attacks.clear()
            piece.white_root_horse_moves.clear()

            piece.white_root_bishop_attacks.clear()
            piece.white_root_bishop_moves.clear()

            piece.white_root_rook_attacks.clear()
            piece.white_root_rook_moves.clear()
            self.pawns = []
            self.white_pawns = []
            self.horses = []
            self.white_horses = []
            self.queen = []
            self.white_queen = []
            self.king = []
            self.white_king = []
            self.rooks = []
            self.white_rooks = []
            self.bishops = []
            self.white_bishops = []
            self.pawnb_num = 0
            self.horseb_num = 0
            self.queenb_num = 0
            self.kingb_num = 0
            self.rookb_num = 0
            self.bishopb_num = 0
            self.b_move_attack.clear()
            self.w_move_attack.clear()


