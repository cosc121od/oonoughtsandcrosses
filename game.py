from board import Board
class Game(object):
    
    def __init__(self, player1, player2):
        self.board = Board()
        self.player1 = player1
        self.player2 = player2
        self.current_player = 2
        
        
    def play(self):
        self.board.display()
        gameover = self.gameover()
        while gameover == False:
            self.next_player()
            is_empty = False
            while is_empty == False:
                if self.current_player == 1:
                    move = self.player1.get_move()
                elif self.current_player == 2:
                    move = self.player2.get_move()
                is_empty = self.board.is_empty(move)
                if is_empty == False:
                    print('There is already a piece in this posistion')
            if self.current_player == 1:
                self.board.set_token(move, self.player1.piece)
            elif self.current_player == 2:
                self.board.set_token(move, self.player2.piece)
            gameover = self.gameover()
            self.board.display()
        if self.is_draw() == False:
            print (self.winner())
        else:
            print("Draw")
            
    def gameover(self):
        is_won = self.is_won()
        is_draw = self.is_draw()
        if is_won == True or is_draw == True:
            return True
        else:
            return False
    
    
    def is_won(self):
        is_won = False
        for row in range(3):
            line = self.board.line(row)
            if self.is_winning_line(line) == True:
                is_won = True
        for col in range(3):
            col += 3
            line = self.board.line(col)
            if self.is_winning_line(line) == True:
                is_won = True
        for diagonal in range(2):
            diagonal += 6
            line = self.board.line(diagonal)
            if self.is_winning_line(line) == True:
                is_won = True
        return is_won
    
    def is_draw(self):
        is_draw = self.board.is_full()
        return is_draw
            
    def is_winning_line(self, line):
        is_winning = False
        if line[0] == line[1] and line[0] == line[2] and line[0] != '-':
            is_winning = True
        return is_winning

    def next_player(self):
        """switches which players turn it is"""
        if self.current_player == 1:
            self.current_player = 2
        elif self.current_player == 2:
            self.current_player = 1
    
    
    def winner(self):
        '''Annonces who won the game'''
        if self.current_player == 1:
            win = self.player1.name
        if self.current_player == 2:
            win = self.player2.name
        return '{} wins'.format(win)
