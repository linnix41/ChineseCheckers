import pygame
from .constants import *
from .board import Board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win
        #self.flag = None
        #self.winner = None

    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def _init(self):        
        self.selected = None
        self.board = Board()
        self.turn = BLUE
        self.valid_moves = {} 

    def reset(self):
        self._init()        
    
    def is_jumped(self, pos1x, pos1y, pos2x, pos2y):
        
        if abs(pos1x - pos2x) == 200 or abs(pos1y - pos2y) == 200:
            self.board.flag = 1
            return True 
            
        else:
            self.board.flag = -1
            return False
              


    def change_turn(self):
        if self.turn == RED: 
            self.turn = BLUE           
        else:
            self.turn = RED    

            