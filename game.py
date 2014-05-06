from board import Board

class Game(object):

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = Board()
    
    def play():
        self.current_player = self.player2
        while (not is_game_over):
            self.next_player()
            move = self.current_player.get_move()
            piece = self.current_player.get_piece()
            self.board.set_point(move, piece)
        print('Game over!')
        self.announce_winner()
    
    def is_game_over():
        return self.is_won() or self.is_draw()

    def next_player():
        if (self.current_player == self.player1):
            self.current_player = self.player2
        else:
            self.current_player = self.player1
      
    def winner():
        return self.current_player

    def is_won():
        return self.board.get_game_state() == 'WIN'
    
    def is_draw():
        return self.board.get_game_state() == 'DRAW'
    
    def announce_winner():
        if (self.is_draw()):
            print('It was a draw.')
        else:
            print('The winner is {}.'.format(self.winner()))
