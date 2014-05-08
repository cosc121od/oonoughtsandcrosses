from board import Board

class Game(object):
    '''A Game object manages the logic of a game of Noughts and Crosses'''

    def __init__(self, player1, player2):
        '''Initialise a game. player1 is assumed to play first.'''
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.board = Board()


    def play(self):
        '''Play a game of noughts and crosses'''
        while not self.game_over():
            self.board.display()
            move_square = self.current_player.get_move(self.board)
            self.board[move_square] = self.current_player.piece
            self.next_player()

        self.board.display()
        if self.is_draw():
            print("Draw!")
        else:
            print("And the winner is ... ", self.winner().name)


    def next_player(self):
        '''Switch the current player'''
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1


    def game_over(self):
        '''True iff the game is over, either because it's a draw or
        there's a winner'''
        return self.is_won() or self.is_draw()


    def is_won(self):
        '''True iff the current game state has a winner, i.e., one
        player has 3 pieces in a row'''
        return any([self.board.is_winning_line(i)
                        for i in Board.ALL_LINES])


    def is_draw(self):
        '''True iff the current game is drawn, i.e. there are no empty
        spaces and no winner'''
        return self.board.is_full() and not self.is_won()


    def winner(self):
        '''Return the player that has won the game. Should only be
        called in the event the game is known to be won. In which case,
        the winner is the player who made the last move.'''
        self.next_player()  # Switch back to the previous player
        return self.current_player





