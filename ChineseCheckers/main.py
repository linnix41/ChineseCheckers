
import pygame
from checkers.constants import *
from checkers.board import *
from checkers.game import Game
from checkers.constants import BLACK
from tkinter import messagebox
from pygame import mixer

pygame.init()
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chinese Checkers")

def get_pos_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col     

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    game.update()
    while run:
        clock.tick(FPS)
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r:
                    game.reset()
                    print("xx")

                if event.key == pygame.K_ESCAPE:
                    run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
            
                pos =  pygame.mouse.get_pos()
                row, col = get_pos_from_mouse(pos)
                print(pos)
                color = WIN.get_at(pos)

                if game.board.flag == 1 and color != BLACK:
                    messagebox.showerror("!", "You can't do this move")
                    continue

                selected_square = game.board.get_piece(row, col)
                
                


                game.update()

                if selected_square != 0 and selected_square.color == game.turn: 
                    
                    game.board.selected_piece = selected_square
                    a,b = col * 100 + 50, row * 100 + 50 
                    game.board.show_valid_moves(game.board.selected_piece, WIN, a, b)
                    
                    
                if color == BLACK:
                    game.board.move(game.board.selected_piece, row, col)
                    piece_sound = mixer.Sound("ChineseCheckers\piece_sound.wav")
                    piece_sound.play()
                    game.update()
                    if game.board.is_over(WIN):
                        messagebox.showinfo("Game is Over", f"The winner is {game.board.winner}")
                        run = False
                        
                    if game.is_jumped(game.board.selected_piece.x, game.board.selected_piece.y, a, b):
                        
                        game.board.show_valid_moves(game.board.selected_piece, WIN, a, b)

                        a, b = game.board.selected_piece.x, game.board.selected_piece.y
                        if game.board.flag == 1:
                            continue
                
                         
                    game.change_turn()
             
                      
              
        
        pygame.display.update()

        
        
    pygame.quit()
main()    