class game(object):
    
    def __init__(self, player1, player2):
        self.palyer1 = player(player1)
        self.player2 = player(player2)
        self.current_player = 2
        self.board = board()
        
    
    def play(self):
        """runs through the game"""
        end = self.game_over()
        while (end == False):
            current_player = next_player()
            if current_player == 1:
                place = self.player1.get_move()
                self.board.set_token(place, self.player1.piece)
            elif current_player == 2:
                place = self.player2.get_move()
                self.board.set_token(place, self.player2.piece)
            end = self.game_over()
                
        
    def game_over(self):
        """tests if the end condition has been met"""
        if self.board.is_full() == True or self.board.is_winning_line() == True:
            self.is_won()
            return True
        else:
            return False
    
    
    def next_player(self):
        """switches which players turn it is"""
        if current_player == 1:
            return 2
        elif current_player == 2:
            return 1
        
    
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
