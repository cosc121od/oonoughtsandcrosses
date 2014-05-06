'''The implementation of the board class'''


class Board(object):
    """Class representing a board object in a game of naughts in crosses"""
    
    EMPTY_BOARD = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    ROWS = [0,1,2]
    COLUMNS = [3,4,5]
    DIAGONALS = [6, 7]
    
    def __init__(self):
        """initialisation"""
        self.board =  Board.EMPTY_BOARD
    
    def get_token(self, coord):
        """return the token at the given coord"""
        return self.board[coord[0]][coord[1]]
        
    def set_token(self, coord, token):
        """set token at given coord"""
        self.board[coord[0]][coord[1]] = token
        
    def is_empty(self, coord):
        """return True if the given coord does not contain a token"""
        return self.board[coord[0]][coord[1]] == '-'
    
    def clear(self):
        """clears the board"""
        self.board = Board.EMPTY_BOARD
        
    def display(self):
        """Display the board"""
        for line in self.board:
            print('|', end='')
            for cell in line:
                print(cell + '|', end='')
            print()
            
    def line(self, num):
        """Return a list representing the line numbered from 0 to 7
        Rows are numbered 0 1 2
        Columns are numbered 3 4 5
        Diagonals are numbered 6 7
        """
        line = []
        if num in Board.ROWS:
            line = self.board[num]
        elif num in Board.COLUMNS:
            for i in range(3):
                line.append(self.board[i][num-3])
        elif num == Board.DIAGONALS[0]:
            for i in range(3):
                line.append(self.board[i][i])
        elif num == Board.DIAGONALS[1]:
            for i in range(3):
                line.append(self.board[i][2-i])
        return line