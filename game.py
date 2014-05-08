from board import Board

class Game(object):

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = Board()
    
    def play(self):
        self.current_player = self.player2
        print(self.board.get_game_state())
        while (not self.is_game_over()):
            self.next_player()
            moved = False
            while (not moved):
                moved = self.request_move()
            print('\n' + str(self.board) + '\n')
        print('Game over man! Game over!')
        self.announce_winner()
    
    def request_move(self):
        move = self.current_player.get_move()
        if (self.board.is_free(move)):
            piece = self.current_player.get_piece()
            self.board.set_point(move, piece)
            return True
        print('That space is taken!')
        return False
    
    def is_game_over(self):
        return self.is_won() or self.is_draw()

    def next_player(self):
        if (self.current_player == self.player1):
            self.current_player = self.player2
        else:
            self.current_player = self.player1
      
    def winner(self):
        return self.current_player

    def is_won(self):
        return self.board.get_game_state() == 'WIN'
    
    def is_draw(self):
        return self.board.get_game_state() == 'DRAW'
    
    def announce_winner(self):
        if (self.is_draw()):
            print('It was a draw.')
        else:
            print('The winner is {}.'.format(self.winner()))
