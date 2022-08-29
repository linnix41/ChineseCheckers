from .constants import *

class Piece:
    PADDING = 12
    radius = SQUARE_SIZE // 2 - PADDING
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.x = 0
        self.y = 0
        

        self.calculate_pos()

    def calculate_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2        
        #print(self.x, self.y)
               
    def draw(self, win):
        #radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


        
    def __repr__(self):
        return str(self.color)

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calculate_pos()    