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
        self.screen = pg.display.set_mode((self.H,self.W))
        

    def update(self):
        pg.display.update()

    def handle_events(self):
        pg.event.set_blocked(pg.MOUSEMOTION)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif pg.mouse.get_pressed()[0] and pg.MOUSEBUTTONUP:
                self.cross.place()
            elif pg.mouse.get_pressed()[2] and pg.MOUSEBUTTONUP:
                self.circle.place()
                
    def draw(self):
        self.cross.draw()
        self.circle.draw()

    def check_three_in_a_row(self):
        totaldict = {}
        counter = 1
        for x in [0,200,400]:
            for y in [0, 200, 400]:
                totaldict[(x,y)] = counter
                counter += 1
        crosslist = self.cross.mark_dict
        circlist = self.circle.mark_dict
        if len(circlist) < 3 and len(crosslist) < 3:
            return False
        else:
            for key, mark in crosslist.items():
                totaldict[key] = "cross"
            for key, mark in circlist.items():
                totaldict[key] = "circle"
            try:
                for x in [0, 200 , 400]:
                    if totaldict[(0,x)] == totaldict[(200,x)] and totaldict[(0,x)] == totaldict[(400,x)]:
                        return True
            except KeyError:
                pass
            try:
                for x in [0, 200 , 400]:
                    if totaldict[(x,0)] == totaldict[(x,200)] and totaldict[(x,0)] == totaldict[(x,400)]:
                        return True
            except KeyError:
                pass
            try:
                if totaldict[(0,0)] == totaldict[(200,200)] and totaldict[(0,0)] == totaldict[(400,400)]:
                    return True
            except KeyError:
                pass
            try:
                if totaldict[(400,0)] == totaldict[(200,200)] and totaldict[(400,0)] == totaldict[(0,400)]:
                    return True
            except KeyError:
                pass
        return False
                
    def restart_if_winner(self):
        if self.check_three_in_a_row():
            self.new_game()

        
    
    def run(self):
        while True:
            self.update()
            self.draw_grid()
            self.handle_events()
            self.restart_if_winner()
            self.draw()

if __name__ == "__main__":
    game = Game()
    game.run()