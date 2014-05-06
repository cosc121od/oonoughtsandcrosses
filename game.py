'''The implementation of the game class'''
class Game(object):
    def __init__(self, player1, player2, current_player, board):
        self.player1 = player()
        self.player2 = player()
        self.current_player = current_player
        self.board = board()
        
    def winner(self):
        '''Annonces who won the game'''
        if self.current_player == 1:
            win = self.player1.name
        if self.current_player == 2:
            win = self.player2.name
        return '{} wins'.format(win)          
        
    def is_won(self):
        '''Sees if game is won'''
        gameover = self.game_over()
        if gameover == True:
            if board.has_winning_line() == True:
                winner()  
            else:
                is_drawn()
    
    def is_drawn(self):
        '''Sees if game has ended in a draw'''    
        return "Game is drawn"       

        
