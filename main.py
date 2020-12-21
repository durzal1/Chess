import pygame
import os
from content.pieces import *
from content.board import *
from content.constants import *
from content.ai_temp import *
from tkinter import *
import time
#STARTED 10/12/2020 FINISHED 11/10/2020 multiplayer
#Started 11/11/2020 Finished 12/21 single player
#took thanksgiving week break and some other breaks for studying
#Anywhere from 40 minutes -3 hours per day mon-thursday
#9th grade
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")
FPS = 60


root = Tk()
root.geometry("300x300")
def click1():
    global multiplayer

    multiplayer = False
    root.destroy()


def click2():
    global multiplayer
    multiplayer = True
    root.destroy()

myButton1 = Button(root, text="single player", command=click1, padx=100, pady=50, fg="white",  bg="blue")  # state=DISABLED
myButton2 = Button(root, text="two player", command=click2, padx=100, pady=50, fg="white",  bg="red")  # state=DISABLED
myButton1.grid(row=0,column=0, pady=10, padx= 15)
myButton2.grid(row=1, column=0)
root.mainloop()



if multiplayer:
    #multiplayer

    def main():
        run = True
        board = Board()
        clock= pygame.time.Clock()
        board.draw_squares(WIN)

        board.draw_piece(WIN)
        while run:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    #board.move(pos, WIN)
                    board.undo(pos, WIN)
                    board.mouse_pressed(pos, WIN)
                    board.win(WIN)




                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass

            pygame.display.update()


else:
    #single player
    def main():
        run = True
        board = Board()
        clock = pygame.time.Clock()
        board.draw_squares(WIN)

        board.draw_piece(WIN)
        pygame.display.update()
        while run:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    # board.move(pos, WIN)
                    board.undo(pos, WIN)
                    board.mouse_pressed(pos, WIN)
                    board.win(WIN)


                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
            if (board.turn_over):
                    board.AI(WIN)
            pygame.display.update()


main()
