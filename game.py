from player import Player
from board import Board

class Game(object):

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = Board()
    
    def play():
        self.current_player = self.player1
    
    def game_over():
        pass

    def next_player():
        if (self.current_player == self.player1):
            self.current_player = self.player2
        else:
            self.current_player = self.player1
      
    def winner():
        return self.current_player

    def is_won():
        pass
    
    def is_draw():
        pass
