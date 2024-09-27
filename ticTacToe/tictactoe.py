#want to make tictactoe oop approach

import pygame as pg
import sys
from game_objects import *

class Game:
    def __init__(self):
        pg.init()
        self.H = 600
        self.W = 600
        self.div = 3
        self.SS = self.H // self.div
        self.screen = pg.display.set_mode((self.H,self.W))
        self.new_game()

    def draw_grid(self):
        for x in range(0,self.W,self.SS):
            pg.draw.line(self.screen,(50,50,50),(x,0),(x,self.H))
        for y in range(0,self.W,self.SS):
            pg.draw.line(self.screen,(50,50,50),(0,y),(self.W,y))

    def new_game(self):
        self.cross = Cross(self,"red")
        self.circle = Circle(self,"green")

    def update(self):
        pg.display.update()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif pg.mouse.get_pressed()[0]:
                self.cross.place()
            elif pg.mouse.get_pressed()[2]:
                self.circle.place()
                
    def draw(self):
        self.cross.draw()
        self.circle.draw()
    
    def run(self):
        while True:
            self.update()
            self.draw_grid()
            self.handle_events()
            self.draw()

if __name__ == "__main__":
    game = Game()
    game.run()