'''The implementation of the board class'''
class Board(object):

    def __init__(self):
        self.dimx = 3
        self.dimy = 3
        self.grid = [['' for i in range(dimy)] for i in range(dimx)]
    
    
    def __str__(self):
        output = ''
        for j in range(self.dimy):
            line = ''
            for i in range(self.dimx):
                line += self.grid[i][j]
                if i != self.dimx-1: line += '|'
            output += line + '\n'
            if j != self.dimy-1:
                line = '-'
                for i in range(self.dimx - 1):
                    line += '+-'
                output += line + '\n'
        return output
    
    def set_point(self, xytuple, value):
        'sets X or O at a point on the board'
        x, y = xytuple
        self.grid[y][x] = value
    
    def get_point(self, xytuple):
        'gets X or O from a point on the board'
        x, y = xytuple
        return self.grid[y][x]
    
    def is_free(self, xytuple):
        'returns true if the position Xytuple on the grid is free'
        return self.grid[y][x] == ''
    
    def get_game_state(self):
        'Does shit get off my back'
        for i in range(dimx):
            row_win = True
            for j in range(1, dimy):
                
        
    
    def reset(self):
        'resets the board'
        self.grid = []
        self.__init__()