'''The implementation of the player class'''
import webbrowser


class Player(object):
    def __init__(self, name, piece):
        self.name = name
        self.piece = piece
        
    def get_move(self):
        move = input("What is your move "+self.name+'? ').lower()
        if move == '42':
            webbrowser.open('http://heyyeyaaeyaaaeyaeyaa.com')
            
        while True:
            
            if self.move_good(move):
                return self.format_move(move)
            else:
                print("invalid, Try again")
                move = input("What is your move "+self.name+'? ').lower()
                
        
    def move_good(self, move):
        if (move[0] == 'a' or move[0] == 'b' or move[0] == 'c') and  \
           (move[1] == '1' or move[1] == '2' or move[1] == '3'):
            return True
        else: 
            return False
        
    def format_move(self, move):
        if move[0]=='a':
            x_move=0
        if move[0]=='b':
            x_move=1
        if move[0]=='c':
            x_move=2            
            
        return (x_move, int(move[1])-1)
            
            
    def __str__(self):
        return self.name
    def get_peice(self):
        return self.piece
