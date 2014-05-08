
class Player(object):
    '''Represents a noughts-and-crosses player. Has a name and a "piece".
    Includes the code to ask the player for their move.'''

    def __init__(self, name, piece):
        '''Initialise the player to the given name and piece, where the
        latter is (usually) X or O'''
        self.name = name
        self.piece = piece

    def get_move(self, board):
        '''Prompt the user for the move by this player.
        Returns a pair (row, column)'''
        result = None
        prompt = "{} ('{}'), enter move (1..9): ".format(self.name, self.piece)
        while result is None:
            move = input(prompt)
            if len(move) == 1 and move[0] in '123456789':
                num = int(move)
                row = (num - 1) // 3
                column = (num - 1) % 3
                if board.is_empty(row, column):
                    result = (row, column)
            if result is None:
                print("Illegal move")
        return result
