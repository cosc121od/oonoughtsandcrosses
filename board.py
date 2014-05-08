'''The Board class for the noughts and crosses game'''

class Board(object):
    '''A Board just represents the 3 x 3 grid on which a Noughts and Crosses
    game is played. It 'knows' nothing about the rules of the game, just how
    to store and display game 'pieces' (usually X and O).
    A Board supports the getitem/setitem interface, where the parameter is
    a (row, column) pair.
    '''

    # Define identifers for rows, columns and lines
    ROWS = [0, 1, 2]
    COLUMNS = [3, 4, 5]
    DIAGONALS = [6, 7]
    ALL_LINES = ROWS + COLUMNS + DIAGONALS

    def __init__(self):
        '''Board initialiser'''
        self.board = [ '---', '---', '---']


    def is_full(self):
        '''True iff all squares are occupied by players pieces'''
        return ''.join(self.board).count('-') == 0


    def __getitem__(self, row_and_col):
        '''Gets the contents of the given row and column'''
        row, column = row_and_col
        return self.board[row][column]


    def __setitem__(self, row_and_col, player_char):
        '''Sets the contents of the square (row, col) to player_char'''
        row, column = row_and_col
        self.board[row] = (self.board[row][:column] + player_char
                            + self.board[row][column + 1:])


    def is_empty(self, row, column):
        '''True iff the given square does not contain a piece'''
        return self[row, column] == '-'


    def is_winning_line(self, line_specifier):
        '''True iff the line of 3 pieces specified by the line_specifier
        is a win, i.e. all same and not empty.
        '''
        chars = self.line(line_specifier)
        char_list = list(chars)
        is_win = (chars != '---' and
                  char_list[1] == char_list[0] and
                  char_list[2] == char_list[0])
        return is_win


    def line(self, line_specifier):
        '''Return a string representing a row, column or diagonal of
        this board, where line_specifier = 0 - 2 are the 3 rows, 3 - 5
        are the 3 columns and 6 and 7 are the two diagonals.'''
        line_string = ''
        if line_specifier in Board.ROWS:
            line_string = self.board[line_specifier]
        elif line_specifier in Board.COLUMNS:
            column = line_specifier - Board.COLUMNS[0]
            line_string = (self[0, column] +
                           self[1, column] +
                           self[2, column])
        elif line_specifier == Board.DIAGONALS[0]:
            line_string = self[0, 0] + self[1, 1] + self[2, 2]
        else:
            assert line_specifier == Board.DIAGONALS[1]
            line_string = self[0, 2] + self[1, 1] + self[2, 0]
        return line_string


    def display(self):
        '''Display the game state on the terminal'''
        print('\n' + str(self)+ '\n')


    def __str__(self):
        '''String representation of a board'''
        return '\n'.join(self.board)







