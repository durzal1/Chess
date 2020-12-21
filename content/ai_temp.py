from content.constants import *
from content.pieces import *
from content.board import *
import pygame
import time
# board.board_temp = ""
class ai:

    def __init__(self):
        pass
    def setup1(board, type2, row, column, color, turn, win):
        global pressed
        # print(type_piece1)
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
        if not (piece.skip):
            if not (piece.pressed):
                if type_piece == classes[1][0]:
                    print("rookw")

                    if board.turn_color == (255, 255, 255):
                        for i in range(8):
                            # add 100 to y
                            row = row
                            new_col = column1 + i + 1
                            if row > 7 or new_col > 7:
                                break
                            if board.board[row][new_col].type1 != "none" and board.board[row][new_col].color == (0,0,0):
                                pygame.draw.circle(win, BLUE, (x, y + (diff * i) + diff), 20)
                                piece.possible_moves.append((str(row), str(new_col), int(x), int(y + (diff * i) + diff)))
                                piece.white_root_rook_moves.append(
                                    [str(row), str(new_col), int(x), int(y + (diff * i) + diff)])
                            elif board.board[row][new_col].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, (x, y + (diff * i) + diff), 20)
                                piece.possible_attacks.append((str(row), str(new_col), int(x), int(y + (diff * i) + diff)))
                                piece.white_root_rook_attacks.append(
                                    [str(row), str(new_col), int(x), int(y + (diff * i) + diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            # subtract 100 to y
                            row = row
                            new_col = column1 - i - 1
                            if row > 7 or new_col > 7:
                                break
                            if board.board[row][new_col].type1 != "none" and board.board[row][new_col].color == (0,0,0):
                                pygame.draw.circle(win, BLUE, (x, y - (diff * i) - diff), 20)
                                piece.possible_moves.append((str(row), str(new_col), int(x), int(y - (diff * i) - diff)))
                                piece.white_root_rook_moves.append(
                                    [str(row), str(new_col), int(x), int(y - (diff * i) - diff)])
                            elif board.board[row][new_col].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, (x, y - (diff * i) - diff), 20)
                                piece.possible_attacks.append((str(row), str(new_col), int(x), int(y - (diff * i) - diff)))
                                piece.white_root_rook_attacks.append(
                                    [str(row), str(new_col), int(x), int(y - (diff * i) - diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            # add 100 to x
                            new_row = row + i + 1
                            col = column1
                            if new_row > 7 or col > 7:
                                break
                            if board.board[new_row][col].type1 != "none" and board.board[new_row][col].color == (0,0,0):
                                pygame.draw.circle(win, BLUE, (x + (diff * i) + diff, y), 20)
                                piece.possible_moves.append((str(new_row), str(col), int(x + (diff * i) + diff), int(y)))
                                piece.white_root_rook_moves.append(
                                    [str(new_row), str(col), int(x + (diff * i) + diff), int(y)])
                            elif board.board[new_row][col].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, (x + (diff * i) + diff, y), 20)
                                piece.possible_attacks.append((str(new_row), str(col), int(x + (diff * i) + diff), int(y)))
                                piece.white_root_rook_attacks.append(
                                    [str(new_row), str(col), int(x + (diff * i) + diff), int(y)])
                                break
                            else:
                                break
                        for i in range(8):
                            # subtract 100 to x
                            new_row = row - i - 1
                            col = column1
                            if new_row > 7 or col > 7:
                                break
                            if board.board[new_row][col].type1 != "none" and  board.board[new_row][col].color == (0,0,0):
                                pygame.draw.circle(win, BLUE, (x - (diff * i) - diff, y), 20)
                                piece.possible_moves.append((str(new_row), str(col), int(x - (diff * i) - diff), int(y)))
                                piece.white_root_rook_moves.append(
                                    [str(new_row), str(col), int(x - (diff * i) - diff), int(y)])
                            elif board.board[new_row][col].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, (x - (diff * i) - diff, y), 20)
                                piece.possible_attacks.append((str(new_row), str(col), int(x - (diff * i) - diff), int(y)))
                                piece.white_root_rook_attacks.append(
                                    [str(new_row), str(col), int(x - (diff * i) - diff), int(y)])
                                break
                            else:
                                break

                        if len(piece.possible_moves) > 0 or len(piece.possible_attacks) > 0:
                            piece.current.extend([row, column])
                            piece.pressed = True
                elif type_piece == classes[0][0]:
                    print("piece.black_attacksokb1")
                    if board.turn_color == (0, 0, 0):
                        for i in range(8):
                            # add 100 to y
                            row = row
                            new_col = column1 + i + 1
                            if row > 7 or new_col > 7:
                                break
                            if board.board[row][new_col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x, y + (diff * i) + diff), 20)
                                piece.possible_moves.append((str(row), str(new_col), int(x), int(y + (diff * i) + diff)))
                                piece.root_rook_moves.append([str(row), str(new_col), int(x), int(y + (diff * i) + diff)])
                            elif board.board[row][new_col].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (x, y + (diff * i) + diff), 20)
                                piece.possible_attacks.append((str(row), str(new_col), int(x), int(y + (diff * i) + diff)))
                                piece.black_attacks.append([str(row), str(new_col), int(x), int(y + (diff * i) + diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            # subtract 100 to y
                            row = row
                            new_col = column1 - i - 1
                            if row > 7 or new_col > 7:
                                break
                            if board.board[row][new_col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x, y - (diff * i) - diff), 20)
                                piece.possible_moves.append((str(row), str(new_col), int(x), int(y - (diff * i) - diff)))
                                piece.root_rook_moves.append([str(row), str(new_col), int(x), int(y - (diff * i) - diff)])
                            elif board.board[row][new_col].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (x, y - (diff * i) - diff), 20)
                                piece.possible_attacks.append((str(row), str(new_col), int(x), int(y - (diff * i) - diff)))
                                piece.black_attacks.append([str(row), str(new_col), int(x), int(y - (diff * i) - diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            # add 100 to x
                            new_row = row + i + 1
                            col = column1
                            if new_row > 7 or col > 7:
                                break
                            if board.board[new_row][col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x + (diff * i) + diff, y), 20)
                                piece.possible_moves.append((str(new_row), str(col), int(x + (diff * i) + diff), int(y)))
                                piece.root_rook_moves.append([str(new_row), str(col), int(x + (diff * i) + diff), int(y)])
                            elif board.board[new_row][col].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (x + (diff * i) + diff, y), 20)
                                piece.possible_attacks.append((str(new_row), str(col), int(x + (diff * i) + diff), int(y)))
                                piece.black_attacks.append([str(new_row), str(col), int(x + (diff * i) + diff), int(y)])
                                break
                            else:
                                break
                        for i in range(8):
                            # subtract 100 to x
                            new_row = row - i - 1
                            col = column1
                            if new_row > 7 or col > 7:
                                break
                            if board.board[new_row][col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x - (diff * i) - diff, y), 20)
                                piece.possible_moves.append((str(new_row), str(col), int(x - (diff * i) - diff), int(y)))
                                piece.root_rook_moves.append([str(new_row), str(col), int(x - (diff * i) - diff), int(y)])
                            elif board.board[new_row][col].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (x - (diff * i) - diff, y), 20)
                                piece.possible_attacks.append((str(new_row), str(col), int(x - (diff * i) - diff), int(y)))
                                piece.black_attacks.append([str(new_row), str(col), int(x - (diff * i) - diff), int(y)])
                                break
                            else:
                                break

                        if len(piece.possible_moves) > 0 or len(piece.possible_attacks) > 0:
                            piece.current.extend([row, column])
                            piece.pressed = True

                elif type_piece == classes[1][1]:
                    print("horsew")
                    if board.turn_color == (255, 255, 255):
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
                            if board.board_temp[row_right1][col_down2].type1 == "none":
                                pygame.draw.circle(win, BLUE, (row_right1 * SQUARE_SIZE + 50, col_down2 * SQUARE_SIZE + 50),
                                                   20)
                                piece.possible_moves.append((str(row_right1), str(col_down2),
                                                             int(row_right1 * SQUARE_SIZE + 50),
                                                             int(col_down2 * SQUARE_SIZE + 50)))
                                piece.white_root_horse_moves.append([str(row_right1), str(col_down2),
                                                                     int(row_right1 * SQUARE_SIZE + 50),
                                                                     int(col_down2 * SQUARE_SIZE + 50)])
                            elif board.board_temp[row_right1][col_down2].color == (0, 0, 0):
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
                            if board.board_temp[row_left1][col_down2].type1 == "none":
                                pygame.draw.circle(win, BLUE, (row_left1 * SQUARE_SIZE + 50, col_down2 * SQUARE_SIZE + 50),
                                                   20)
                                piece.possible_moves.append((str(row_left1), str(col_down2),
                                                             int(row_left1 * SQUARE_SIZE + 50),
                                                             int(col_down2 * SQUARE_SIZE + 50)))
                                piece.white_root_horse_moves.append([str(row_left1), str(col_down2),
                                                                     int(row_left1 * SQUARE_SIZE + 50),
                                                                     int(col_down2 * SQUARE_SIZE + 50)])
                            elif board.board_temp[row_left1][col_down2].color == (0, 0, 0):
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
                            if board.board_temp[row_left2][col_down1].type1 == "none":
                                pygame.draw.circle(win, BLUE, (row_left2 * SQUARE_SIZE + 50, col_down1 * SQUARE_SIZE + 50),
                                                   20)
                                piece.possible_moves.append((str(row_left2), str(col_down1),
                                                             int(row_left2 * SQUARE_SIZE + 50),
                                                             int(col_down1 * SQUARE_SIZE + 50)))
                                piece.white_root_horse_moves.append([str(row_left2), str(col_down1),
                                                                     int(row_left2 * SQUARE_SIZE + 50),
                                                                     int(col_down1 * SQUARE_SIZE + 50)])
                            elif board.board_temp[row_left2][col_down1].color == (0, 0, 0):
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
                            if board.board_temp[row_left2][col_up1].type1 == "none":
                                pygame.draw.circle(win, BLUE, (row_left2 * SQUARE_SIZE + 50, col_up1 * SQUARE_SIZE + 50),
                                                   20)
                                piece.possible_moves.append((
                                    str(row_left2), str(col_up1), int(row_left2 * SQUARE_SIZE + 50),
                                    int(col_up1 * SQUARE_SIZE + 50)))
                                piece.white_root_horse_moves.append(
                                    [str(row_left2), str(col_up1), int(row_left2 * SQUARE_SIZE + 50),
                                     int(col_up1 * SQUARE_SIZE + 50)])
                            elif board.board_temp[row_left2][col_up1].color == (0, 0, 0):
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
                            if board.board_temp[row_left1][col_up2].type1 == "none":
                                pygame.draw.circle(win, BLUE, (row_left1 * SQUARE_SIZE + 50, col_up2 * SQUARE_SIZE + 50),
                                                   20)
                                piece.possible_moves.append((
                                    str(row_left1), str(col_up2), int(row_left1 * SQUARE_SIZE + 50),
                                    int(col_up2 * SQUARE_SIZE + 50)))
                                piece.white_root_horse_moves.append([
                                    str(row_left1), str(col_up2), int(row_left1 * SQUARE_SIZE + 50),
                                    int(col_up2 * SQUARE_SIZE + 50)])
                            elif board.board_temp[row_left1][col_up2].color == (0, 0, 0):
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
                            if board.board_temp[row_right1][col_up2].type1 == "none":
                                pygame.draw.circle(win, BLUE, (row_right1 * SQUARE_SIZE + 50, col_up2 * SQUARE_SIZE + 50),
                                                   20)
                                piece.possible_moves.append((str(row_right1), str(col_up2),
                                                             int(row_right1 * SQUARE_SIZE + 50),
                                                             int(col_up2 * SQUARE_SIZE + 50)))
                                piece.white_root_horse_moves.append([str(row_right1), str(col_up2),
                                                                     int(row_right1 * SQUARE_SIZE + 50),
                                                                     int(col_up2 * SQUARE_SIZE + 50)])
                            elif board.board_temp[row_right1][col_up2].color == (0, 0, 0):
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
                            if board.board_temp[row_right2][col_up1].type1 == "none":
                                pygame.draw.circle(win, BLUE, (row_right2 * SQUARE_SIZE + 50, col_up1 * SQUARE_SIZE + 50),
                                                   20)
                                piece.possible_moves.append((str(row_right2), str(col_up1),
                                                             int(row_right2 * SQUARE_SIZE + 50),
                                                             int(col_up1 * SQUARE_SIZE + 50)))
                                piece.white_root_horse_moves.append([str(row_right2), str(col_up1),
                                                                     int(row_right2 * SQUARE_SIZE + 50),
                                                                     int(col_up1 * SQUARE_SIZE + 50)])
                            elif board.board_temp[row_right2][col_up1].color == (0, 0, 0):
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
                            if board.board_temp[row_right2][col_down1].type1 == "none":
                                pygame.draw.circle(win, BLUE, (row_right2 * SQUARE_SIZE + 50, col_down1 * SQUARE_SIZE + 50),
                                                   20)
                                piece.possible_moves.append((str(row_right2), str(col_down1),
                                                             int(row_right2 * SQUARE_SIZE + 50),
                                                             int(col_down1 * SQUARE_SIZE + 50)))
                                piece.white_root_horse_moves.append([str(row_right2), str(col_down1),
                                                                     int(row_right2 * SQUARE_SIZE + 50),
                                                                     int(col_down1 * SQUARE_SIZE + 50)])
                            elif board.board_temp[row_right2][col_down1].color == (0, 0, 0):
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
                    if board.turn_color == (0, 0, 0):
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
                            if board.board[row_right1][col_down2].type1 == "none":
                                pygame.draw.circle(win, BLUE, (row_right1 * SQUARE_SIZE + 50, col_down2 * SQUARE_SIZE + 50),
                                                   20)
                                piece.possible_moves.append((str(row_right1), str(col_down2),
                                                             int(row_right1 * SQUARE_SIZE + 50),
                                                             int(col_down2 * SQUARE_SIZE + 50)))
                                piece.root_horse_moves.append(
                                    [str(row_right1), str(col_down2), int(row_right1 * SQUARE_SIZE + 50),
                                     int(col_down2 * SQUARE_SIZE + 50)])
                            elif board.board[row_right1][col_down2].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN,
                                                   (row_right1 * SQUARE_SIZE + 50, col_down2 * SQUARE_SIZE + 50), 20)
                                piece.possible_attacks.append((str(row_right1), str(col_down2),
                                                               int(row_right1 * SQUARE_SIZE + 50),
                                                               int(col_down2 * SQUARE_SIZE + 50)))
                                piece.black_attacks.append(
                                    [str(row_right1), str(col_down2), int(row_right1 * SQUARE_SIZE + 50),
                                     int(col_down2 * SQUARE_SIZE + 50)])
                        if row_left1 > 7 or row_left1 < 0 or col_down2 > 7 or col_down2 < 0:
                            pass
                        else:
                            if board.board[row_left1][col_down2].type1 == "none":
                                pygame.draw.circle(win, BLUE, (row_left1 * SQUARE_SIZE + 50, col_down2 * SQUARE_SIZE + 50),
                                                   20)
                                piece.possible_moves.append((str(row_left1), str(col_down2),
                                                             int(row_left1 * SQUARE_SIZE + 50),
                                                             int(col_down2 * SQUARE_SIZE + 50)))
                                piece.root_horse_moves.append(
                                    [str(row_left1), str(col_down2), int(row_left1 * SQUARE_SIZE + 50),
                                     int(col_down2 * SQUARE_SIZE + 50)])
                            elif board.board[row_left1][col_down2].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (row_left1 * SQUARE_SIZE + 50, col_down2 * SQUARE_SIZE + 50),
                                                   20)
                                piece.possible_attacks.append((str(row_left1), str(col_down2),
                                                               int(row_left1 * SQUARE_SIZE + 50),
                                                               int(col_down2 * SQUARE_SIZE + 50)))
                                piece.black_attacks.append(
                                    [str(row_left1), str(col_down2), int(row_left1 * SQUARE_SIZE + 50),
                                     int(col_down2 * SQUARE_SIZE + 50)])
                        if row_left2 > 7 or row_left2 < 0 or col_down1 > 7 or col_down1 < 0:
                            pass
                        else:
                            if board.board[row_left2][col_down1].type1 == "none":
                                pygame.draw.circle(win, BLUE, (row_left2 * SQUARE_SIZE + 50, col_down1 * SQUARE_SIZE + 50),
                                                   20)
                                piece.possible_moves.append((str(row_left2), str(col_down1),
                                                             int(row_left2 * SQUARE_SIZE + 50),
                                                             int(col_down1 * SQUARE_SIZE + 50)))
                                piece.root_horse_moves.append(
                                    [str(row_left2), str(col_down1), int(row_left2 * SQUARE_SIZE + 50),
                                     int(col_down1 * SQUARE_SIZE + 50)])
                            elif board.board[row_left2][col_down1].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (row_left2 * SQUARE_SIZE + 50, col_down1 * SQUARE_SIZE + 50),
                                                   20)
                                piece.possible_attacks.append((str(row_left2), str(col_down1),
                                                               int(row_left2 * SQUARE_SIZE + 50),
                                                               int(col_down1 * SQUARE_SIZE + 50)))
                                piece.black_attacks.append(
                                    [str(row_left2), str(col_down1), int(row_left2 * SQUARE_SIZE + 50),
                                     int(col_down1 * SQUARE_SIZE + 50)])
                        if row_left2 > 7 or row_left2 < 0 or col_up1 > 7 or col_up1 < 0:
                            pass
                        else:
                            if board.board[row_left2][col_up1].type1 == "none":
                                pygame.draw.circle(win, BLUE, (row_left2 * SQUARE_SIZE + 50, col_up1 * SQUARE_SIZE + 50),
                                                   20)
                                piece.possible_moves.append((
                                                            str(row_left2), str(col_up1), int(row_left2 * SQUARE_SIZE + 50),
                                                            int(col_up1 * SQUARE_SIZE + 50)))
                                piece.root_horse_moves.append(
                                    [str(row_left2), str(col_up1), int(row_left2 * SQUARE_SIZE + 50),
                                     int(col_up1 * SQUARE_SIZE + 50)])
                            elif board.board[row_left2][col_up1].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (row_left2 * SQUARE_SIZE + 50, col_up1 * SQUARE_SIZE + 50),
                                                   20)
                                piece.possible_attacks.append((str(row_left2), str(col_up1),
                                                               int(row_left2 * SQUARE_SIZE + 50),
                                                               int(col_up1 * SQUARE_SIZE + 50)))
                                piece.black_attacks.append(
                                    [str(row_left2), str(col_up1), int(row_left2 * SQUARE_SIZE + 50),
                                     int(col_up1 * SQUARE_SIZE + 50)])
                        if row_left1 > 7 or row_left1 < 0 or col_up2 > 7 or col_up2 < 0:
                            pass
                        else:
                            if board.board[row_left1][col_up2].type1 == "none":
                                pygame.draw.circle(win, BLUE, (row_left1 * SQUARE_SIZE + 50, col_up2 * SQUARE_SIZE + 50),
                                                   20)
                                piece.possible_moves.append((
                                                            str(row_left1), str(col_up2), int(row_left1 * SQUARE_SIZE + 50),
                                                            int(col_up2 * SQUARE_SIZE + 50)))
                                piece.root_horse_moves.append(
                                    [str(row_left1), str(col_up2), int(row_left1 * SQUARE_SIZE + 50),
                                     int(col_up2 * SQUARE_SIZE + 50)])
                            elif board.board[row_left1][col_up2].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (row_left1 * SQUARE_SIZE + 50, col_up2 * SQUARE_SIZE + 50),
                                                   20)
                                piece.possible_attacks.append((str(row_left1), str(col_up2),
                                                               int(row_left1 * SQUARE_SIZE + 50),
                                                               int(col_up2 * SQUARE_SIZE + 50)))
                                piece.black_attacks.append(
                                    [str(row_left1), str(col_up2), int(row_left1 * SQUARE_SIZE + 50),
                                     int(col_up2 * SQUARE_SIZE + 50)])
                        if row_right1 > 7 or row_right1 < 0 or col_up2 > 7 or col_up2 < 0:
                            pass
                        else:
                            if board.board[row_right1][col_up2].type1 == "none":
                                pygame.draw.circle(win, BLUE, (row_right1 * SQUARE_SIZE + 50, col_up2 * SQUARE_SIZE + 50),
                                                   20)
                                piece.possible_moves.append(
                                    [str(row_right1), str(col_up2), int(row_right1 * SQUARE_SIZE + 50),
                                     int(col_up2 * SQUARE_SIZE + 50)])
                                piece.root_horse_moves.append(
                                    [str(row_right1), str(col_up2), int(row_right1 * SQUARE_SIZE + 50),
                                     int(col_up2 * SQUARE_SIZE + 50)])
                            elif board.board[row_right1][col_up2].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (row_right1 * SQUARE_SIZE + 50, col_up2 * SQUARE_SIZE + 50),
                                                   20)
                                piece.possible_attacks.append((str(row_right1), str(col_up2),
                                                               int(row_right1 * SQUARE_SIZE + 50),
                                                               int(col_up2 * SQUARE_SIZE + 50)))
                                piece.black_attacks.append(
                                    [str(row_right1), str(col_up2), int(row_right1 * SQUARE_SIZE + 50),
                                     int(col_up2 * SQUARE_SIZE + 50)])
                        if row_right2 > 7 or row_right2 < 0 or col_up1 > 7 or col_up1 < 0:
                            pass
                        else:
                            if board.board[row_right2][col_up1].type1 == "none":
                                pygame.draw.circle(win, BLUE, (row_right2 * SQUARE_SIZE + 50, col_up1 * SQUARE_SIZE + 50),
                                                   20)
                                piece.possible_moves.append((str(row_right2), str(col_up1),
                                                             int(row_right2 * SQUARE_SIZE + 50),
                                                             int(col_up1 * SQUARE_SIZE + 50)))
                                piece.root_horse_moves.append(
                                    [str(row_right2), str(col_up1), int(row_right2 * SQUARE_SIZE + 50),
                                     int(col_up1 * SQUARE_SIZE + 50)])
                            elif board.board[row_right2][col_up1].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (row_right2 * SQUARE_SIZE + 50, col_up1 * SQUARE_SIZE + 50),
                                                   20)
                                piece.possible_attacks.append((str(row_right2), str(col_up1),
                                                               int(row_right2 * SQUARE_SIZE + 50),
                                                               int(col_up1 * SQUARE_SIZE + 50)))
                                piece.black_attacks.append(
                                    [str(row_right2), str(col_up1), int(row_right2 * SQUARE_SIZE + 50),
                                     int(col_up1 * SQUARE_SIZE + 50)])
                        if row_right2 > 7 or row_right2 < 0 or col_down1 > 7 or col_down1 < 0:
                            pass
                        else:
                            if board.board[row_right2][col_down1].type1 == "none":
                                pygame.draw.circle(win, BLUE, (row_right2 * SQUARE_SIZE + 50, col_down1 * SQUARE_SIZE + 50),
                                                   20)
                                piece.possible_moves.append((str(row_right2), str(col_down1),
                                                             int(row_right2 * SQUARE_SIZE + 50),
                                                             int(col_down1 * SQUARE_SIZE + 50)))
                                piece.root_horse_moves.append(
                                    [str(row_right2), str(col_down1), int(row_right2 * SQUARE_SIZE + 50),
                                     int(col_down1 * SQUARE_SIZE + 50)])
                            elif board.board[row_right2][col_down1].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN,
                                                   (row_right2 * SQUARE_SIZE + 50, col_down1 * SQUARE_SIZE + 50), 20)
                                piece.possible_attacks.append((str(row_right2), str(col_down1),
                                                               int(row_right2 * SQUARE_SIZE + 50),
                                                               int(col_down1 * SQUARE_SIZE + 50)))
                                piece.black_attacks.append(
                                    [str(row_right2), str(col_down1), int(row_right2 * SQUARE_SIZE + 50),
                                     int(col_down1 * SQUARE_SIZE + 50)])
                        if len(piece.possible_moves) > 0 or len(piece.possible_attacks) > 0:
                            piece.current.extend([row, column])
                            piece.pressed = True

                elif type_piece == classes[1][2]:
                    print("bishopw")
                    if board.turn_color == (255, 255, 255):
                        for i in range(8):
                            # add 100 to y and x
                            new_row = row + i + 1
                            new_col = column1 + i + 1
                            if new_row > 7 or new_col > 7:
                                break
                            if board.board_temp[new_row][new_col].type1 != "none" and board.board_temp[new_row][new_col].color == (0,0,0):
                                pygame.draw.circle(win, BLUE, ((x + (diff * i) + diff), y + (diff * i) + diff), 20)
                                piece.possible_moves.append(
                                    (str(new_row), str(new_col), int(x + (diff * i) + diff), int(y + (diff * i) + diff)))
                                piece.white_root_bishop_moves.append(
                                    [str(new_row), str(new_col), int(x + (diff * i) + diff), int(y + (diff * i) + diff)])
                            elif board.board_temp[new_row][new_col].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, ((x + (diff * i) + diff), y + (diff * i) + diff), 20)
                                piece.possible_attacks.append(
                                    (str(new_row), str(new_col), int(x + (diff * i) + diff), int(y + (diff * i) + diff)))
                                piece.white_root_bishop_attacks.append(
                                    [str(new_row), str(new_col), int(x + (diff * i) + diff), int(y + (diff * i) + diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            # subtract 100 to y and subtract 100 to x
                            new_row = row - i - 1
                            new_col = column1 - i - 1
                            if new_row > 7 or new_col > 7:
                                break
                            if board.board_temp[new_row][new_col].type1 != "none" and board.board_temp[new_row][new_col].color == (0,0,0):
                                pygame.draw.circle(win, BLUE, (x - (diff * i) - diff, y - (diff * i) - diff), 20)
                                piece.possible_moves.append(
                                    (str(new_row), str(new_col), int(x - (diff * i) - diff), int(y - (diff * i) - diff)))
                                piece.white_root_bishop_moves.append(
                                    [str(new_row), str(new_col), int(x - (diff * i) - diff), int(y - (diff * i) - diff)])
                            elif board.board_temp[new_row][new_col].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, (x - (diff * i) - diff, y - (diff * i) - diff), 20)
                                piece.possible_attacks.append(
                                    (str(new_row), str(new_col), int(x - (diff * i) - diff), int(y - (diff * i) - diff)))
                                piece.white_root_bishop_attacks.append(
                                    [str(new_row), str(new_col), int(x - (diff * i) - diff), int(y - (diff * i) - diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            # add 100 to x and subtract 100 to y
                            new_row = row + i + 1
                            new_col = column1 - i - 1
                            if new_row > 7 or new_col > 7:
                                break
                            if board.board_temp[new_row][new_col].type1 !=  "none" and board.board_temp[new_row][new_col].color ==  (0,0,0):
                                pygame.draw.circle(win, BLUE, (x + (diff * i) + diff, y - (diff * i) - diff), 20)
                                piece.possible_moves.append(
                                    (str(new_row), str(new_col), int(x + (diff * i) + diff), int(y - (diff * i) - diff)))
                                piece.white_root_bishop_moves.append(
                                    [str(new_row), str(new_col), int(x + (diff * i) + diff), int(y - (diff * i) - diff)])
                            elif board.board_temp[new_row][new_col].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, (x + (diff * i) + diff, y - (diff * i) - diff), 20)
                                piece.possible_attacks.append(
                                    (str(new_row), str(new_col), int(x + (diff * i) + diff), int(y - (diff * i) - diff)))
                                piece.white_root_bishop_attacks.append(
                                    [str(new_row), str(new_col), int(x + (diff * i) + diff), int(y - (diff * i) - diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            # subtract 100 to x and add 100 to y
                            new_row = row - i - 1
                            new_col = column1 + i + 1
                            if new_row > 7 or new_col > 7:
                                break
                            if board.board_temp[new_row][new_col].type1 !=  "none" and board.board_temp[new_row][new_col].color ==  (0,0,0):
                                pygame.draw.circle(win, BLUE, (x - (diff * i) - diff, y + (diff * i) + diff), 20)
                                piece.possible_moves.append(
                                    (str(new_row), str(new_col), int(x - (diff * i) - diff), int(y + (diff * i) + diff)))
                                piece.white_root_bishop_moves.append(
                                    [str(new_row), str(new_col), int(x - (diff * i) - diff), int(y + (diff * i) + diff)])

                            elif board.board_temp[new_row][new_col].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, (x - (diff * i) - diff, y + (diff * i) + diff), 20)
                                piece.possible_attacks.append(
                                    (str(new_row), str(new_col), int(x - (diff * i) - diff), int(y + (diff * i) + diff)))
                                piece.white_root_bishop_attacks.append(
                                    [str(new_row), str(new_col), int(x - (diff * i) - diff), int(y + (diff * i) + diff)])
                                break
                            else:
                                break
                        if len(piece.possible_moves) > 0 or len(piece.possible_attacks) > 0:
                            piece.current.extend([row, column])
                            piece.pressed = True
                elif type_piece == classes[0][2]:
                    print("bishopb")
                    if board.turn_color == (0, 0, 0):
                        for i in range(8):
                            # add 100 to y and x
                            new_row = row + i + 1
                            new_col = column1 + i + 1
                            if new_row > 7 or new_col > 7:
                                break
                            if board.board[new_row][new_col].type1 == "none":
                                pygame.draw.circle(win, BLUE, ((x + (diff * i) + diff), y + (diff * i) + diff), 20)
                                piece.possible_moves.append(
                                    (str(new_row), str(new_col), int(x + (diff * i) + diff), int(y + (diff * i) + diff)))
                                piece.root_bishop_moves.append(
                                    [str(new_row), str(new_col), int(x + (diff * i) + diff), int(y + (diff * i) + diff)])
                            elif board.board[new_row][new_col].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, ((x + (diff * i) + diff), y + (diff * i) + diff), 20)

                                piece.black_attacks.append(
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
                            if board.board[new_row][new_col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x - (diff * i) - diff, y - (diff * i) - diff), 20)
                                piece.possible_moves.append(
                                    (str(new_row), str(new_col), int(x - (diff * i) - diff), int(y - (diff * i) - diff)))
                                piece.root_bishop_moves.append(
                                    [
                                        str(new_row), str(new_col), int(x - (diff * i) - diff), int(y - (diff * i) - diff)])
                            elif board.board[new_row][new_col].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (x - (diff * i) - diff, y - (diff * i) - diff), 20)

                                piece.black_attacks.append(
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
                            if board.board[new_row][new_col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x + (diff * i) + diff, y - (diff * i) - diff), 20)
                                piece.possible_moves.append(
                                    (str(new_row), str(new_col), int(x + (diff * i) + diff), int(y - (diff * i) - diff)))
                                piece.root_bishop_moves.append(
                                    [
                                        str(new_row), str(new_col), int(x + (diff * i) + diff), int(y - (diff * i) - diff)])
                            elif board.board[new_row][new_col].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (x + (diff * i) + diff, y - (diff * i) - diff), 20)

                                piece.black_attacks.append(
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
                            if board.board[new_row][new_col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x - (diff * i) - diff, y + (diff * i) + diff), 20)
                                piece.possible_moves.append(
                                    (str(new_row), str(new_col), int(x - (diff * i) - diff), int(y + (diff * i) + diff)))
                                piece.root_bishop_moves.append(
                                    [
                                        str(new_row), str(new_col), int(x - (diff * i) - diff), int(y + (diff * i) + diff)])
                            elif board.board[new_row][new_col].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (x - (diff * i) - diff, y + (diff * i) + diff), 20)

                                piece.black_attacks.append(
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
                    if board.turn_color == (255, 255, 255):
                        for i in range(8):
                            # add 100 to y and x
                            new_row = row + i + 1
                            new_col = column1 + i + 1
                            if new_row > 7 or new_col > 7:
                                break
                            if board.board_temp[new_row][new_col].type1 != "none" and board.board_temp[new_row][new_col].color == (0,0,0):
                                pygame.draw.circle(win, BLUE, ((x + (diff * i) + diff), y + (diff * i) + diff), 20)
                                piece.possible_moves.append(
                                    (str(new_row), str(new_col), int(x + (diff * i) + diff), int(y + (diff * i) + diff)))
                                piece.white_root_queen_moves.append(
                                    [str(new_row), str(new_col), int(x + (diff * i) + diff), int(y + (diff * i) + diff)])
                            elif board.board_temp[new_row][new_col].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, ((x + (diff * i) + diff), y + (diff * i) + diff), 20)
                                piece.possible_attacks.append(
                                    (str(new_row), str(new_col), int(x + (diff * i) + diff), int(y + (diff * i) + diff)))
                                piece.white_root_queen_attacks.append(
                                    [str(new_row), str(new_col), int(x + (diff * i) + diff), int(y + (diff * i) + diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            # subtract 100 to y and subtract 100 to x
                            new_row = row - i - 1
                            new_col = column1 - i - 1
                            if new_row > 7 or new_col > 7:
                                break
                            if board.board_temp[new_row][new_col].type1 != "none" and board.board_temp[new_row][new_col].color == (0,0,0):
                                pygame.draw.circle(win, BLUE, (x - (diff * i) - diff, y - (diff * i) - diff), 20)
                                piece.possible_moves.append(
                                    (str(new_row), str(new_col), int(x - (diff * i) - diff), int(y - (diff * i) - diff)))
                                piece.white_root_queen_moves.append(
                                    [str(new_row), str(new_col), int(x - (diff * i) - diff), int(y - (diff * i) - diff)])
                            elif board.board_temp[new_row][new_col].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, (x - (diff * i) - diff, y - (diff * i) - diff), 20)
                                piece.possible_attacks.append(
                                    (str(new_row), str(new_col), int(x - (diff * i) - diff), int(y - (diff * i) - diff)))
                                piece.white_root_queen_attacks.append(
                                    [str(new_row), str(new_col), int(x - (diff * i) - diff), int(y - (diff * i) - diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            # add 100 to x and subtract 100 to y
                            new_row = row + i + 1
                            new_col = column1 - i - 1
                            if new_row > 7 or new_col > 7:
                                break
                            if board.board_temp[new_row][new_col].type1 != "none" and  board.board_temp[new_row][new_col].color == (0,0,0):
                                pygame.draw.circle(win, BLUE, (x + (diff * i) + diff, y - (diff * i) - diff), 20)
                                piece.possible_moves.append(
                                    (str(new_row), str(new_col), int(x + (diff * i) + diff), int(y - (diff * i) - diff)))
                                piece.white_root_queen_moves.append(
                                    [str(new_row), str(new_col), int(x + (diff * i) + diff), int(y - (diff * i) - diff)])
                            elif board.board_temp[new_row][new_col].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, (x + (diff * i) + diff, y - (diff * i) - diff), 20)
                                piece.possible_attacks.append(
                                    (str(new_row), str(new_col), int(x + (diff * i) + diff), int(y - (diff * i) - diff)))
                                piece.white_root_queen_attacks.append(
                                    [str(new_row), str(new_col), int(x + (diff * i) + diff), int(y - (diff * i) - diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            # subtract 100 to x and add 100 to y
                            new_row = row - i - 1
                            new_col = column1 + i + 1
                            if new_row > 7 or new_col > 7:
                                break
                            if board.board_temp[new_row][new_col].type1 != "none" and  board.board_temp[new_row][new_col].color == (0,0,0):
                                pygame.draw.circle(win, BLUE, (x - (diff * i) - diff, y + (diff * i) + diff), 20)
                                piece.possible_moves.append(
                                    (str(new_row), str(new_col), int(x - (diff * i) - diff), int(y + (diff * i) + diff)))
                                piece.white_root_queen_moves.append(
                                    [str(new_row), str(new_col), int(x - (diff * i) - diff), int(y + (diff * i) + diff)])
                            elif board.board_temp[new_row][new_col].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, (x - (diff * i) - diff, y + (diff * i) + diff), 20)
                                piece.white_root_queen_attacks.append(
                                    [str(new_row), str(new_col), int(x - (diff * i) - diff), int(y + (diff * i) + diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            # add 100 to y
                            row = row
                            new_col = column1 + i + 1
                            if row > 7 or new_col > 7:
                                break
                            if board.board_temp[row][new_col].type1 != "none" and board.board_temp[row][new_col].color == (0,0,0):
                                pygame.draw.circle(win, BLUE, (x, y + (diff * i) + diff), 20)
                                piece.possible_moves.append((str(row), str(new_col), int(x), int(y + (diff * i) + diff)))
                                piece.white_root_queen_moves.append(
                                    [str(row), str(new_col), int(x), int(y + (diff * i) + diff)])
                            elif board.board_temp[row][new_col].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, (x, y + (diff * i) + diff), 20)
                                piece.possible_attacks.append((str(row), str(new_col), int(x), int(y + (diff * i) + diff)))
                                piece.white_root_queen_attacks.append(
                                    [str(row), str(new_col), int(x), int(y + (diff * i) + diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            # subtract 100 to y
                            row = row
                            new_col = column1 - i - 1
                            if row > 7 or new_col > 7:
                                break
                            if board.board_temp[row][new_col].type1 != "none" and board.board_temp[row][new_col].color == (0,0,0):
                                pygame.draw.circle(win, BLUE, (x, y - (diff * i) - diff), 20)
                                piece.possible_moves.append((str(row), str(new_col), int(x), int(y - (diff * i) - diff)))
                                piece.white_root_queen_moves.append(
                                    [str(row), str(new_col), int(x), int(y - (diff * i) - diff)])
                            elif board.board_temp[row][new_col].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, (x, y - (diff * i) - diff), 20)
                                piece.possible_attacks.append((str(row), str(new_col), int(x), int(y - (diff * i) - diff)))
                                piece.white_root_queen_attacks.append(
                                    [str(row), str(new_col), int(x), int(y - (diff * i) - diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            # add 100 to x
                            new_row = row + i + 1
                            col = column1
                            if new_row > 7 or col > 7:
                                break
                            if board.board_temp[new_row][col].type1 != "none" and board.board_temp[new_row][col].color == (0,0,0):
                                pygame.draw.circle(win, BLUE, (x + (diff * i) + diff, y), 20)
                                piece.possible_moves.append((str(new_row), str(col), int(x + (diff * i) + diff), int(y)))
                                piece.white_root_queen_moves.append(
                                    [str(new_row), str(col), int(x + (diff * i) + diff), int(y)])
                            elif board.board_temp[new_row][col].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, (x + (diff * i) + diff, y), 20)
                                piece.possible_attacks.append((str(new_row), str(col), int(x + (diff * i) + diff), int(y)))
                                piece.white_root_queen_attacks.append(
                                    [str(new_row), str(col), int(x + (diff * i) + diff), int(y)])
                                break
                            else:
                                break
                        for i in range(8):
                            # subtract 100 to x
                            new_row = row - i - 1
                            col = column1
                            if new_row > 7 or col > 7:
                                break
                            if board.board_temp[new_row][col].type1 != "none" and board.board_temp[new_row][col].color == (0,0,0):
                                pygame.draw.circle(win, BLUE, (x - (diff * i) - diff, y), 20)
                                piece.possible_moves.append((str(new_row), str(col), int(x - (diff * i) - diff), int(y)))
                                piece.white_root_queen_moves.append(
                                    [str(new_row), str(col), int(x - (diff * i) - diff), int(y)])
                            elif board.board_temp[new_row][col].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, (x - (diff * i) - diff, y), 20)
                                piece.possible_attacks.append((str(new_row), str(col), int(x - (diff * i) - diff), int(y)))
                                piece.white_root_queen_attacks.append(
                                    [str(new_row), str(col), int(x - (diff * i) - diff), int(y)])
                                break
                            else:
                                break

                        if len(piece.possible_moves) > 0 or len(piece.possible_attacks) > 0:
                            piece.current.extend([row, column])
                            piece.pressed = True
                elif type_piece == classes[0][3]:
                    print("queenb")
                    if board.turn_color == (0, 0, 0):
                        for i in range(8):
                            # add 100 to y and x
                            new_row = row + i + 1
                            new_col = column1 + i + 1
                            if new_row > 7 or new_col > 7:
                                break
                            if board.board[new_row][new_col].type1 == "none":
                                pygame.draw.circle(win, BLUE, ((x + (diff * i) + diff), y + (diff * i) + diff), 20)
                                piece.possible_moves.append(
                                    (str(new_row), str(new_col), int(x + (diff * i) + diff), int(y + (diff * i) + diff)))
                                piece.black_attacks.append(
                                    [str(new_row), str(new_col), int(x + (diff * i) + diff), int(y + (diff * i) + diff)])
                            elif board.board[new_row][new_col].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, ((x + (diff * i) + diff), y + (diff * i) + diff), 20)
                                piece.possible_attacks.append(
                                    (str(new_row), str(new_col), int(x + (diff * i) + diff), int(y + (diff * i) + diff)))
                                piece.root_queen_attacks.append(
                                    [str(new_row), str(new_col), int(x + (diff * i) + diff), int(y + (diff * i) + diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            # subtract 100 to y and subtract 100 to x
                            new_row = row - i - 1
                            new_col = column1 - i - 1
                            if new_row > 7 or new_col > 7:
                                break
                            if board.board[new_row][new_col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x - (diff * i) - diff, y - (diff * i) - diff), 20)
                                piece.possible_moves.append(
                                    (str(new_row), str(new_col), int(x - (diff * i) - diff), int(y - (diff * i) - diff)))
                                piece.root_queen_moves.append(
                                    [str(new_row), str(new_col), int(x - (diff * i) - diff), int(y - (diff * i) - diff)])
                            elif board.board[new_row][new_col].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (x - (diff * i) - diff, y - (diff * i) - diff), 20)

                                piece.black_attacks.append(
                                    [str(new_row), str(new_col), int(x - (diff * i) - diff), int(y - (diff * i) - diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            # add 100 to x and subtract 100 to y
                            new_row = row + i + 1
                            new_col = column1 - i - 1
                            if new_row > 7 or new_col > 7:
                                break
                            if board.board[new_row][new_col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x + (diff * i) + diff, y - (diff * i) - diff), 20)
                                piece.possible_moves.append(
                                    (str(new_row), str(new_col), int(x + (diff * i) + diff), int(y - (diff * i) - diff)))
                                piece.root_queen_moves.append(
                                    [str(new_row), str(new_col), int(x + (diff * i) + diff), int(y - (diff * i) - diff)])
                            elif board.board[new_row][new_col].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (x + (diff * i) + diff, y - (diff * i) - diff), 20)
                                piece.possible_attacks.append(
                                    (str(new_row), str(new_col), int(x + (diff * i) + diff), int(y - (diff * i) - diff)))
                                piece.black_attacks.append(
                                    [str(new_row), str(new_col), int(x + (diff * i) + diff), int(y - (diff * i) - diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            # subtract 100 to x and add 100 to y
                            new_row = row - i - 1
                            new_col = column1 + i + 1
                            if new_row > 7 or new_col > 7:
                                break
                            if board.board[new_row][new_col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x - (diff * i) - diff, y + (diff * i) + diff), 20)
                                piece.possible_moves.append(
                                    (str(new_row), str(new_col), int(x - (diff * i) - diff), int(y + (diff * i) + diff)))
                                piece.root_queen_moves.append(
                                    [str(new_row), str(new_col), int(x - (diff * i) - diff), int(y + (diff * i) + diff)])
                            elif board.board[new_row][new_col].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (x - (diff * i) - diff, y + (diff * i) + diff), 20)

                                piece.black_attacks.append(
                                    [str(new_row), str(new_col), int(x - (diff * i) - diff), int(y + (diff * i) + diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            # add 100 to y
                            row = row
                            new_col = column1 + i + 1
                            if row > 7 or new_col > 7:
                                break
                            if board.board[row][new_col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x, y + (diff * i) + diff), 20)
                                piece.possible_moves.append((str(row), str(new_col), int(x), int(y + (diff * i) + diff)))
                                piece.root_queen_moves.append([str(row), str(new_col), int(x), int(y + (diff * i) + diff)])
                            elif board.board[row][new_col].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (x, y + (diff * i) + diff), 20)
                                piece.possible_attacks.append((str(row), str(new_col), int(x), int(y + (diff * i) + diff)))
                                piece.black_attacks.append(
                                    [str(row), str(new_col), int(x), int(y + (diff * i) + diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            # subtract 100 to y
                            row = row
                            new_col = column1 - i - 1
                            if row > 7 or new_col > 7:
                                break
                            if board.board[row][new_col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x, y - (diff * i) - diff), 20)
                                piece.possible_moves.append((str(row), str(new_col), int(x), int(y - (diff * i) - diff)))
                                piece.root_queen_moves.append([str(row), str(new_col), int(x), int(y - (diff * i) - diff)])
                            elif board.board[row][new_col].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (x, y - (diff * i) - diff), 20)
                                piece.black_attacks.append([str(row), str(new_col), int(x), int(y - (diff * i) - diff)])
                                break
                            else:
                                break
                        for i in range(8):
                            # add 100 to x
                            new_row = row + i + 1
                            col = column1
                            if new_row > 7 or col > 7:
                                break
                            if board.board[new_row][col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x + (diff * i) + diff, y), 20)
                                piece.possible_moves.append((str(new_row), str(col), int(x + (diff * i) + diff), int(y)))
                                piece.root_queen_moves.append([str(new_row), str(col), int(x + (diff * i) + diff), int(y)])
                            elif board.board[new_row][col].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (x + (diff * i) + diff, y), 20)
                                piece.black_attacks.append(
                                    [str(new_row), str(col), int(x + (diff * i) + diff), int(y)])
                                break
                            else:
                                break
                        for i in range(8):
                            # subtract 100 to x
                            new_row = row - i - 1
                            col = column1
                            if new_row > 7 or col > 7:
                                break
                            if board.board[new_row][col].type1 == "none":
                                pygame.draw.circle(win, BLUE, (x - (diff * i) - diff, y), 20)
                                piece.possible_moves.append((str(new_row), str(col), int(x - (diff * i) - diff), int(y)))
                                piece.root_queen_moves.append([str(new_row), str(col), int(x - (diff * i) - diff), int(y)])
                            elif board.board[new_row][col].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (x - (diff * i) - diff, y), 20)
                                piece.black_attacks.append(
                                    [str(new_row), str(col), int(x - (diff * i) - diff), int(y)])
                                break
                            else:
                                break

                        if len(piece.possible_moves) > 0 or len(piece.possible_attacks) > 0:
                            piece.current.extend([row, column])
                            piece.pressed = True
                elif type_piece == classes[1][4]:
                    print("kingw")
                    if board.turn_color == (255, 255, 255):
                        new_col_same = column
                        new_col_up = column - 1
                        new_col_down = column + 1
                        new_row_same = row
                        new_row_left = row - 1
                        new_row_right = row + 1
                        print(row, new_col_down)
                        if board.board_temp[row][new_col_up].type1 == "none":
                            # up 1
                            pygame.draw.circle(win, BLUE, (x, y - diff), 20)
                            piece.possible_moves.append(((str(row), str(new_col_up), int(x), int(y - diff))))
                            piece.white_root_king_moves.append([str(row), str(new_col_up), int(x), int(y - diff)])
                        elif board.board_temp[row][new_col_up].color == (0, 0, 0):
                            print('y')
                            pygame.draw.circle(win, GREEN, (x, y - diff), 20)
                            piece.possible_attacks.append(((str(row), str(new_col_up), int(x), int(y - diff))))
                            piece.white_root_king_attacks.append([str(row), str(new_col_up), int(x), int(y - diff)])
                        if new_col_down < 0 or new_col_down > 7:
                            pass
                        else:
                            if board.board_temp[row][new_col_down].type1 == "none":
                                # down 1
                                pygame.draw.circle(win, BLUE, (x, y + diff), 20)
                                piece.possible_moves.append(((str(row), str(new_col_down), int(x), int(y + diff))))
                                piece.white_root_king_moves.append([str(row), str(new_col_down), int(x), int(y + diff)])
                            elif board.board_temp[row][new_col_down].color == (0, 0, 0):
                                # down 1
                                pygame.draw.circle(win, GREEN, (x, y + diff), 20)
                                piece.possible_attacks.append(((str(row), str(new_col_down), int(x), int(y + diff))))
                                piece.white_root_king_attacks.append([str(row), str(new_col_down), int(x), int(y + diff)])
                        if new_row_right < 0 or new_row_right > 7:
                            pass
                        else:
                            if board.board_temp[new_row_right][column].type1 == "none":
                                # right 1
                                pygame.draw.circle(win, BLUE, (x + diff, y), 20)
                                piece.possible_moves.append(((str(new_row_right), str(column), int(x + diff), int(y))))
                                piece.white_root_king_moves.append([str(new_row_right), str(column), int(x + diff), int(y)])
                            elif board.board_temp[new_row_right][column].color == (0, 0, 0):
                                # right 1
                                pygame.draw.circle(win, GREEN, (x + diff, y), 20)
                                piece.possible_attacks.append(((str(new_row_right), str(column), int(x + diff), int(y))))
                                piece.white_root_king_attacks.append(
                                    [str(new_row_right), str(column), int(x + diff), int(y)])
                        if board.board_temp[new_row_left][column].type1 == "none":
                            # left 1
                            pygame.draw.circle(win, BLUE, (x - diff, y), 20)
                            piece.possible_moves.append(((str(new_row_left), str(column), int(x - diff), int(y))))
                            piece.white_root_king_moves.append([str(new_row_left), str(column), int(x - diff), int(y)])
                        elif board.board_temp[new_row_left][column].color == (0, 0, 0):
                            # left 1
                            pygame.draw.circle(win, GREEN, (x - diff, y), 20)
                            piece.possible_attacks.append(((str(new_row_left), str(column), int(x - diff), int(y))))
                            piece.white_root_king_attacks.append([str(new_row_left), str(column), int(x - diff), int(y)])
                        if new_row_right < 0 or new_row_right > 7 or new_col_down < 0 or new_col_down > 7:
                            pass
                        else:
                            if board.board_temp[new_row_right][new_col_down].type1 == "none":
                                # down 1 right 1
                                pygame.draw.circle(win, BLUE, (x + diff, y + diff), 20)
                                piece.possible_moves.append(
                                    ((str(new_row_right), str(new_col_down), int(x + diff), int(y + diff))))
                                piece.white_root_king_moves.append(
                                    [str(new_row_right), str(new_col_down), int(x + diff), int(y + diff)])
                            elif board.board_temp[new_row_right][new_col_down].color == (0, 0, 0):
                                # down 1 right 1
                                pygame.draw.circle(win, GREEN, (x + diff, y + diff), 20)
                                piece.possible_attacks.append(
                                    ((str(new_row_right), str(new_col_down), int(x + diff), int(y + diff))))
                                piece.white_root_king_attacks.append(
                                    [str(new_row_right), str(new_col_down), int(x + diff), int(y + diff)])
                        if new_row_right < 0 or new_row_right > 7:
                            pass
                        else:
                            if board.board_temp[new_row_right][new_col_up].type1 == "none":
                                # up 1 right 1
                                pygame.draw.circle(win, BLUE, (x + diff, y - diff), 20)
                                piece.possible_moves.append(
                                    ((str(new_row_right), str(new_col_up), int(x + diff), int(y - diff))))
                                piece.white_root_king_moves.append(
                                    [str(new_row_right), str(new_col_up), int(x + diff), int(y - diff)])
                            elif board.board_temp[new_row_right][new_col_up].color == (0, 0, 0):
                                # up 1 right 1
                                pygame.draw.circle(win, GREEN, (x + diff, y - diff), 20)
                                piece.possible_attacks.append(
                                    ((str(new_row_right), str(new_col_up), int(x + diff), int(y - diff))))
                                piece.white_root_king_attacks.append(
                                    [str(new_row_right), str(new_col_up), int(x + diff), int(y - diff)])
                        if new_col_down > 7 or new_col_down < 0:
                            pass
                        else:
                            if board.board_temp[new_row_left][new_col_down].type1 == "none":
                                # down 1 left 1
                                pygame.draw.circle(win, BLUE, (x - diff, y + diff), 20)
                                piece.possible_moves.append(
                                    ((str(new_row_left), str(new_col_down), int(x - diff), int(y + diff))))
                                piece.white_root_king_moves.append(
                                    [str(new_row_left), str(new_col_down), int(x - diff), int(y + diff)])
                            elif board.board_temp[new_row_left][new_col_down].color == (0, 0, 0):
                                # down 1 left 1
                                pygame.draw.circle(win, GREEN, (x - diff, y + diff), 20)
                                piece.possible_attacks.append(
                                    ((str(new_row_left), str(new_col_down), int(x - diff), int(y + diff))))
                                piece.white_root_king_attacks.append(
                                    [str(new_row_left), str(new_col_down), int(x - diff), int(y + diff)])
                        if board.board_temp[new_row_left][new_col_up].type1 == "none":
                            # up 1 left 1
                            pygame.draw.circle(win, BLUE, (x - diff, y - diff), 20)
                            piece.possible_moves.append(
                                ((str(new_row_left), str(new_col_up), int(x - diff), int(y - diff))))
                            piece.white_root_king_moves.append(
                                [str(new_row_left), str(new_col_up), int(x - diff), int(y - diff)])
                        elif board.board_temp[new_row_left][new_col_up].color == (0, 0, 0):
                            # up 1 left 1
                            pygame.draw.circle(win, GREEN, (x - diff, y - diff), 20)
                            piece.possible_attacks.append(
                                ((str(new_row_left), str(new_col_up), int(x - diff), int(y - diff))))
                            piece.white_root_king_attacks.append(
                                [str(new_row_left), str(new_col_up), int(x - diff), int(y - diff)])

                        if len(piece.possible_moves) > 0 or len(piece.possible_attacks) > 0:
                            piece.current.extend([row, column])
                            piece.pressed = True
                elif type_piece == classes[0][4]:
                    print("kingb")
                    if board.turn_color == (0, 0, 0):
                        new_col_same = column
                        new_col_up = column - 1
                        new_col_down = column + 1
                        new_row_same = row
                        new_row_left = row - 1
                        new_row_right = row + 1
                        print(row, new_col_down)
                        if board.board[row][new_col_up].type1 == "none":
                            # up 1
                            pygame.draw.circle(win, BLUE, (x, y - diff), 20)
                            piece.possible_moves.append(((str(row), str(new_col_up), int(x), int(y - diff))))
                            piece.root_king_moves.append([str(row), str(new_col_up), int(x), int(y - diff)])
                        elif board.board[row][new_col_up].color == (255, 255, 255):
                            pygame.draw.circle(win, GREEN, (x, y - diff), 20)
                            piece.possible_attacks.append(((str(row), str(new_col_up), int(x), int(y - diff))))
                            piece.black_attacks.append([str(row), str(new_col_up), int(x), int(y - diff)])
                        if new_col_down < 0 or new_col_down > 7:
                            pass
                        else:
                            if board.board[row][new_col_down].type1 == "none":
                                # down 1
                                pygame.draw.circle(win, BLUE, (x, y + diff), 20)
                                piece.possible_moves.append(((str(row), str(new_col_down), int(x), int(y + diff))))
                                piece.root_king_moves.append([str(row), str(new_col_down), int(x), int(y + diff)])
                            elif board.board[row][new_col_down].color == (255, 255, 255):
                                # down 1
                                pygame.draw.circle(win, GREEN, (x, y + diff), 20)
                                piece.possible_attacks.append(((str(row), str(new_col_down), int(x), int(y + diff))))
                                piece.black_attacks.append([str(row), str(new_col_down), int(x), int(y + diff)])
                        if new_row_right < 0 or new_row_right > 7:
                            pass
                        else:
                            if board.board[new_row_right][column].type1 == "none":
                                # right 1
                                pygame.draw.circle(win, BLUE, (x + diff, y), 20)
                                piece.possible_moves.append(((str(new_row_right), str(column), int(x + diff), int(y))))
                                piece.root_king_moves.append([str(new_row_right), str(column), int(x + diff), int(y)])
                            elif board.board[new_row_right][column].color == (255, 255, 255):
                                # right 1
                                pygame.draw.circle(win, GREEN, (x + diff, y), 20)
                                piece.possible_attacks.append(((str(new_row_right), str(column), int(x + diff), int(y))))
                                piece.black_attacks.append([str(new_row_right), str(column), int(x + diff), int(y)])
                        if board.board[new_row_left][column].type1 == "none":
                            # left 1
                            pygame.draw.circle(win, BLUE, (x - diff, y), 20)
                            piece.possible_moves.append(((str(new_row_left), str(column), int(x - diff), int(y))))
                            piece.root_king_moves.append([str(new_row_left), str(column), int(x - diff), int(y)])
                        elif board.board[new_row_left][column].color == (255, 255, 255):
                            # left 1
                            pygame.draw.circle(win, GREEN, (x - diff, y), 20)
                            piece.possible_attacks.append(((str(new_row_left), str(column), int(x - diff), int(y))))
                            piece.black_attacks.append([str(new_row_left), str(column), int(x - diff), int(y)])
                        if new_row_right < 0 or new_row_right > 7 or new_col_down < 0 or new_col_down > 7:
                            pass
                        else:
                            if board.board[new_row_right][new_col_down].type1 == "none":
                                # down 1 right 1
                                pygame.draw.circle(win, BLUE, (x + diff, y + diff), 20)
                                piece.possible_moves.append(
                                    ((str(new_row_right), str(new_col_down), int(x + diff), int(y + diff))))
                                piece.root_king_moves.append(
                                    [str(new_row_right), str(new_col_down), int(x + diff), int(y + diff)])
                            elif board.board[new_row_right][new_col_down].color == (255, 255, 255):
                                # down 1 right 1
                                pygame.draw.circle(win, GREEN, (x + diff, y + diff), 20)

                                piece.black_attacks.append(
                                    [str(new_row_right), str(new_col_down), int(x + diff), int(y + diff)])
                        if new_row_right < 0 or new_row_right > 7:
                            pass
                        else:
                            if board.board[new_row_right][new_col_up].type1 == "none":
                                # up 1 right 1
                                pygame.draw.circle(win, BLUE, (x + diff, y - diff), 20)
                                piece.possible_moves.append(
                                    ((str(new_row_right), str(new_col_up), int(x + diff), int(y - diff))))
                                piece.root_king_moves.append(
                                    [str(new_row_right), str(new_col_up), int(x + diff), int(y - diff)])
                            elif board.board[new_row_right][new_col_up].color == (255, 255, 255):
                                # up 1 right 1
                                pygame.draw.circle(win, GREEN, (x + diff, y - diff), 20)

                                piece.black_attacks.append(
                                    [str(new_row_right), str(new_col_up), int(x + diff), int(y - diff)])
                        if new_col_down > 7 or new_col_down < 0:
                            pass
                        else:
                            if board.board[new_row_left][new_col_down].type1 == "none":
                                # down 1 left 1
                                pygame.draw.circle(win, BLUE, (x - diff, y + diff), 20)
                                piece.possible_moves.append(
                                    ((str(new_row_left), str(new_col_down), int(x - diff), int(y + diff))))
                                piece.root_king_moves.append(
                                    [str(new_row_left), str(new_col_down), int(x - diff), int(y + diff)])
                            elif board.board[new_row_left][new_col_down].color == (255, 255, 255):
                                # down 1 left 1
                                pygame.draw.circle(win, GREEN, (x - diff, y + diff), 20)

                                piece.black_attacks.append(
                                    [str(new_row_left), str(new_col_down), int(x - diff), int(y + diff)])
                        if board.board[new_row_left][new_col_up].type1 == "none":
                            # up 1 left 1
                            pygame.draw.circle(win, BLUE, (x - diff, y - diff), 20)
                            piece.possible_moves.append(
                                ((str(new_row_left), str(new_col_up), int(x - diff), int(y - diff))))
                            piece.root_king_moves.append([str(new_row_left), str(new_col_up), int(x - diff), int(y - diff)])
                        elif board.board[new_row_left][new_col_up].color == (255, 255, 255):
                            # up 1 left 1
                            pygame.draw.circle(win, GREEN, (x - diff, y - diff), 20)

                            piece.black_attacks.append(
                                [str(new_row_left), str(new_col_up), int(x - diff), int(y - diff)])

                        if len(piece.possible_moves) > 0 or len(piece.possible_attacks) > 0:
                            piece.current.extend([row, column])
                            piece.pressed = True

                elif type_piece == classes[1][5]:
                    print("pawnw")
                    if board.turn_color == (255, 255, 255):
                        print("dadawdadawda")
                        new_col1 = column1 - 1
                        new_col2 = column1 - 2
                        try:
                            if_first_move = board.board_temp[row][column].first_move
                        except Exception:
                            pass
                        attack_row_right = row + 1
                        attack_row_left = row - 1
                        if row + 1 > 7 or column - 1 < 0:
                            print("error1")
                        else:
                            if board.board_temp[attack_row_right][new_col1].type1 != "none" and board.board_temp[attack_row_right][
                                new_col1].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, (x + diff, y - diff), 20)
                                piece.possible_attacks.append(
                                    ((str(attack_row_right), str(new_col1), int(x + diff), int(y - diff))))
                                piece.white_root_pawn_attacks.append(
                                    [str(attack_row_right), str(new_col1), int(x + diff), int(y - diff)])
                        if row - 1 < 0 or column - 1 < 0:
                            print("error2")

                        else:
                            print(column)
                            if board.board_temp[attack_row_left][new_col1].type1 != "none" and board.board_temp[attack_row_left][
                                new_col1].color == (0, 0, 0):
                                pygame.draw.circle(win, GREEN, (x - diff, y - diff), 20)
                                piece.possible_attacks.append(
                                    ((str(attack_row_left), str(new_col1), int(x - diff), int(y - diff))))
                                piece.white_root_pawn_attacks.append(
                                    [str(attack_row_left), str(new_col1), int(x - diff), int(y - diff)])
                        if column - 1 > 7:
                            pass
                        else:
                            if board.board_temp[row][new_col1].type1 == "none":
                                try:
                                    if if_first_move:
                                        print(x, y)
                                        pygame.draw.circle(win, BLUE, (x, y - diff), 20)
                                        pygame.draw.circle(win, BLUE, (x, y - diff * 2), 20)
                                        print("dwadawd")
                                        piece.possible_moves.extend(((str(row1), str(new_col1), int(x), int(y - diff)), (
                                        str(row1), str(new_col2), int(x), int(y - diff * 2)),))
                                        piece.white_root_pawn_moves.extend(
                                            [[str(row1), str(new_col1), int(x), int(y - diff)],
                                             [str(row1), str(new_col2), int(x), int(y - diff * 2)], ])

                                    else:

                                        pygame.draw.circle(win, BLUE, (x, y - diff), 20)
                                        piece.possible_moves.append((str(row1), str(new_col1), int(x), int(y - diff)))
                                        piece.white_root_pawn_moves.append(
                                            [str(row1), str(new_col1), int(x), int(y - diff)])
                                except Exception:
                                    pass
                            if row == 0:
                                if board.board_temp[row][column - 1].type1 == "none":
                                    print(column)
                                    try:
                                        if if_first_move:
                                            pygame.draw.circle(win, BLUE, (x, y - diff), 20)
                                            pygame.draw.circle(win, BLUE, (x, y - diff * 2), 20)
                                            piece.possible_moves.extend(
                                                [(str(row1), str(new_col1), int(x), int(y - diff)),
                                                 (str(row1), str(new_col2), int(x), int(y - diff * 2)), ])
                                            piece.white_root_pawn_moves.extend(
                                                [[str(row1), str(new_col1), int(x), int(y - diff)],
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
                    if board.turn_color == (0, 0, 0):
                        try:
                            if_first_move = board.board[row][column].first_move
                        except Exception:
                            pass

                        new_col1 = column1 + 1
                        new_col2 = column1 + 2

                        attack_row_right = row + 1
                        attack_row_left = row - 1
                        if row + 1 > 7 or column + 1 > 7:
                            pass
                        else:
                            if board.board[attack_row_right][new_col1].type1 != "none" and board.board[attack_row_right][
                                new_col1].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (x + diff, y + diff), 20)
                                piece.possible_attacks.append(
                                    ((str(attack_row_right), str(new_col1), int(x + diff), int(y + diff))))
                                piece.black_attacks.append(
                                    ([str(attack_row_right), str(new_col1), int(x + diff), int(y + diff)]))
                        if row - 1 < 0 or column + 1 > 7:
                            pass
                        else:
                            print(column)
                            if board.board[attack_row_left][new_col1].type1 != "none" and board.board[attack_row_left][
                                new_col1].color == (255, 255, 255):
                                pygame.draw.circle(win, GREEN, (x - diff, y + diff), 20)

                                piece.black_attacks.append(
                                    ([str(attack_row_left), str(new_col1), int(x - diff), int(y + diff)]))
                        if row - 1 < 0 or column + 1 > 7:
                            pass
                        else:
                            if board.board[row][new_col1].type1 == "none":
                                try:
                                    if if_first_move:
                                        pygame.draw.circle(win, BLUE, (x, y + diff), 20)
                                        pygame.draw.circle(win, BLUE, (x, y + diff * 2), 20)
                                        piece.possible_moves.extend(((str(row1), str(new_col1), int(x), int(y + diff)), (
                                        str(row1), str(new_col2), int(x), int(y + diff * 2)),))
                                        piece.root_pawn_moves.extend([[str(row1), str(new_col1), int(x), int(y + diff)],
                                                                      [str(row1), str(new_col2), int(x),
                                                                       int(y + diff * 2)], ])

                                    else:
                                        pygame.draw.circle(win, BLUE, (x, y + diff), 20)
                                        piece.possible_moves.append((str(row1), str(new_col1), int(x), int(y + diff)))
                                        piece.root_pawn_moves.append([str(row1), str(new_col1), int(x), int(y + diff)])
                                except Exception:
                                    pygame.draw.circle(win, BLUE, (x, y + diff), 20)
                                    piece.possible_moves.append((str(row1), str(new_col1), int(x), int(y + diff)))
                                    piece.root_pawn_moves.append([str(row1), str(new_col1), int(x), int(y + diff)])
                        if row == 0:
                            if board.board[row][column + 1].type1 == "none":
                                print(column)
                                try:
                                    if if_first_move:
                                        pygame.draw.circle(win, BLUE, (x, y + diff), 20)
                                        pygame.draw.circle(win, BLUE, (x, y + diff * 2), 20)
                                        piece.possible_moves.extend([(str(row1), str(new_col1), int(x), int(y + diff)),
                                                                     (str(row1), str(new_col2), int(x),
                                                                      int(y + diff * 2)), ])
                                        piece.root_pawn_moves.extend([[str(row1), str(new_col1), int(x), int(y + diff)],
                                                                      [
                                                                          str(row1), str(new_col2), int(x),
                                                                          int(y + diff * 2)], ])

                                    else:
                                        pygame.draw.circle(win, BLUE, (x, y + diff), 20)
                                        piece.root_pawn_attacks.append([str(row1), str(new_col1), int(x), int(y + diff)])
                                except Exception:
                                    pygame.draw.circle(win, BLUE, (x, y + diff), 20)

                        if len(piece.possible_moves) > 0 or len(piece.possible_attacks) > 0:
                            piece.current.extend([row, column])
                            piece.pressed = True
                elif type_piece == classes[1][6] or type_piece == classes[0][6]:
                    print("none")
        else:
            piece.skip = False