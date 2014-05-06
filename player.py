'''The implementation of the player class'''
class Player(object):
    
    def __init__(self, name, piece):
        self.name = name
        self.piece = piece
        
    def get_move(self):
        row = int(input())
        column = int(input())
        x_y = row,column
        return x_y
