import pygame
from .constants import *
from .piece import Piece


class Board:

    PADDING = 13
    radius = SQUARE_SIZE // 2 - PADDING
    

    def __init__(self):
        self.board = []
        self.flag = None
        self.selected_piece = None
        self.create_pieces()
        self.color = None
        self.winner = None
        self.check = None
 
    def draw_squares(self, win):
        #we actaully just drawing lines -_-
        win.fill(BOARD_COLOR)
        #vertical lines
        for row in range(1,ROW):
            pygame.draw.line(win, LINE_COLOR, (SQUARE_SIZE * row, 0), (row * SQUARE_SIZE, HEIGHT), LINE_WIDTH)         


        #horizontal lines
        for col in range(1,COL):
            pygame.draw.line(win, LINE_COLOR, (0, SQUARE_SIZE * col ), (WIDTH, SQUARE_SIZE * col), LINE_WIDTH)         
              
    def draw_valid_moves(self, win, x, y):
        pygame.draw.circle(win, BLACK, (x, y), self.radius)

    def create_pieces(self):
        for row in range(ROW):
            self.board.append([])
            for col in range(COL):
                if col < 3 and row < 3:
                    self.board[row].append(Piece(row, col, RED))
                elif col > 4 and row > 4:
                    self.board[row].append(Piece(row, col, BLUE))     
                else:
                    self.board[row].append(0)    
    
    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROW):
            for col in range(COL):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win) 

    def get_piece(self, row, col):
            return self.board[row][col]
    
    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

    def is_over(self, win):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == 0 or win.get_at(((col * 100 + 50),(row * 100 + 50))) == RED:
                    self.winner = False
                    break
        if self.winner != False:           
            self.winner = "BLUE"
            return True 
        self.winner = None               
        for row in range(5, 8):
            for col in range(5, 8):
                if self.board[row][col] == 0 or win.get_at(((col * 100 + 50),(row * 100 + 50))) == BLUE: #self.board[row][col] == BLUE:
                    self.winner = False
                    break
        if self.winner != False:
            self.winner = "RED"
            return True
        self.winner = None


    def show_valid_moves(self, piece, win, a, b):
        self.check = -1
        if piece.color == BLUE:
            if self.flag != 1:
            
                if piece.row - 1 >= 0 and self.board[piece.row-1][piece.col] == 0:
                    #print("top")
                    self.draw_valid_moves(win, piece.x, piece.y - 100)

                elif piece.row - 2 >= 0 and self.board[piece.row-1][piece.col] != 0 and self.board[piece.row-2][piece.col] == 0:
                    self.draw_valid_moves(win, piece.x, piece.y - 200)

                if piece.row -1 >= 0 and piece.col -1 >= 0 and self.board[piece.row-1][piece.col-1] == 0:   
                    #print("left diagnol")
                    self.draw_valid_moves(win, piece.x - 100, piece.y - 100)


                if piece.row -1 >= 0 and piece.col + 1 <= 7 and self.board[piece.row-1][piece.col+1] == 0:  
                    #print("right diagnol")       
                    self.draw_valid_moves(win, piece.x + 100, piece.y - 100)

                if piece.row + 1 <= 7 and piece.col -1 >= 0 and self.board[piece.row+1][piece.col-1] == 0:
                    #bottom left diagnol
                    self.draw_valid_moves(win, piece.x - 100, piece.y + 100)    

                if piece.col - 1 >= 0 and self.board[piece.row][piece.col-1] == 0:   
                    #print("left ")
                    self.draw_valid_moves(win, piece.x - 100, piece.y)

                elif piece.col - 2 >= 0 and self.board[piece.row][piece.col-1] != 0 and self.board[piece.row][piece.col-2] == 0:
                    self.draw_valid_moves(win, piece.x - 200, piece.y)

                if piece.col + 1 <= 7 and self.board[piece.row][piece.col+1] == 0:    
                    #print("right ")
                    self.draw_valid_moves(win, piece.x + 100, piece.y)

                elif piece.col + 2 <= 7 and self.board[piece.row][piece.col+1] != 0 and self.board[piece.row][piece.col+2] == 0:
                    self.draw_valid_moves(win, piece.x + 200, piece.y)

            else: #jumped
                if piece.row - 2 >= 0 and self.board[piece.row-1][piece.col] != 0 and self.board[piece.row-2][piece.col] == 0:
                    self.draw_valid_moves(win, piece.x, piece.y - 200)  #top jump
                    self.check = 1
                    
                if piece.col - 2 >= 0 and self.board[piece.row][piece.col-1] != 0 and self.board[piece.row][piece.col-2] == 0:
                    if piece.x - 200 != a:
                        self.draw_valid_moves(win, piece.x - 200, piece.y) #left jump
                        self.check = 1

                if piece.col + 2 <= 7 and self.board[piece.row][piece.col+1] != 0 and self.board[piece.row][piece.col+2] == 0:
                    if piece.x + 200 != a:
                        self.draw_valid_moves(win, piece.x + 200, piece.y)    
                        self.check = 1

                if self.check != 1:
                    self.flag = -1

        if piece.color == RED:
            if self.flag != 1:
                if piece.row + 1  <= 7 and self.board[piece.row+1][piece.col] == 0:
                    #print("top")
                    self.draw_valid_moves(win, piece.x, piece.y + 100)

                elif piece.row + 2 <= 7 and self.board[piece.row+1][piece.col] != 0 and self.board[piece.row+2][piece.col] == 0:
                    self.draw_valid_moves(win, piece.x, piece.y + 200)

                if piece.row + 1 <= 7 and piece.col + 1 <= 7 and self.board[piece.row+1][piece.col+1] == 0:   
                    #print("left diagnol")
                    self.draw_valid_moves(win, piece.x + 100, piece.y + 100)

                
                if piece.row + 1 <= 7 and piece.col - 1 >= 0 and self.board[piece.row+1][piece.col-1] == 0:  
                    #print("right diagnol")       
                    self.draw_valid_moves(win, piece.x - 100, piece.y + 100)

                if piece.row -1  >= 0 and piece.col + 1 <= 7 and self.board[piece.row-1][piece.col+1] == 0:
                    #bottom left diagnol
                    self.draw_valid_moves(win, piece.x + 100, piece.y - 100)

                if piece.col + 1 <= 7 and self.board[piece.row][piece.col+1] == 0:   
                    #print("left ")
                    self.draw_valid_moves(win, piece.x + 100, piece.y)

                elif piece.col + 2 <= 7 and self.board[piece.row][piece.col+1] != 0 and self.board[piece.row][piece.col+2] == 0:
                    self.draw_valid_moves(win, piece.x + 200, piece.y)

                if piece.col - 1 >= 0 and self.board[piece.row][piece.col-1] == 0:    
                    #print("right ")
                    self.draw_valid_moves(win, piece.x - 100, piece.y)        

                elif piece.col - 2 >= 0 and self.board[piece.row][piece.col-1] != 0 and self.board[piece.row][piece.col-2] == 0:
                    self.draw_valid_moves(win, piece.x - 200, piece.y)    

            else: #jumped
                if piece.row + 2 <= 7 and self.board[piece.row+1][piece.col] != 0 and self.board[piece.row+2][piece.col] == 0:
                    self.draw_valid_moves(win, piece.x, piece.y + 200)
                    self.check = 1
                
                if piece.col + 2 <= 7 and self.board[piece.row][piece.col+1] != 0 and self.board[piece.row][piece.col+2] == 0:
                    if piece.x + 200 != a:
                        self.draw_valid_moves(win, piece.x + 200, piece.y)
                        self.check = 1

                if piece.col - 2 >= 0 and self.board[piece.row][piece.col-1] != 0 and self.board[piece.row][piece.col-2] == 0:
                    if piece.x - 200 !=a:
                        self.draw_valid_moves(win, piece.x - 200, piece.y)    
                        self.check = 1

                if self.check != 1:
                    self.flag = -1        