import pygame as pg

class Marker:
    def __init__(self,game,color):
        self.game = game
        self.screen = game.screen
        self.H = game.H
        self.W = game.W
        self.div = game.div
        self.SS = self.H // self.div
        self.color = color
        self.mark_dict = {}

    def round_to_ss(self,num):
        return num[0] - num[0] % self.SS, num[1] - num[1] % self.SS

    

    def draw(self):
        for key,mark in self.mark_dict.items():
            pg.draw.rect(self.screen,self.color,mark)

    

class Cross(Marker):
    def place(self):
        mp0,mp1 = self.round_to_ss(pg.mouse.get_pos())
        if not self.check_if_taken(mp0,mp1):
            rect = pg.Rect(mp0,mp1, self.SS,self.SS)
            self.mark_dict[(mp0,mp1)] = rect

    def check_if_taken(self,mp0,mp1):
        return (mp0,mp1) in self.game.circle.mark_dict


class Circle(Marker):
    def place(self):
        mp0,mp1 = self.round_to_ss(pg.mouse.get_pos())
        if not self.check_if_taken(mp0,mp1):
            rect = pg.Rect(mp0,mp1, self.SS,self.SS)
            self.mark_dict[(mp0,mp1)] = rect

    def check_if_taken(self,mp0,mp1):
        return (mp0,mp1) in self.game.cross.mark_dict
