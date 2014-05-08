'''The implementation of the board class'''
class Board(object):

    def __init__(self):
        self.dimx = 3
        self.dimy = 3
        self.grid = [['' for i in range(self.dimy)] for i in range(self.dimx)]
    
    
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
        self.print_grid()
    
    def get_point(self, xytuple):
        'gets X or O from a point on the board'
        x, y = xytuple
        return self.grid[y][x]
    
    def is_free(self, xytuple):
        'returns true if the position Xytuple on the grid is free'
        return self.grid[y][x] == ''
    
    def get_game_state(self):
        """returns 'WIN', 'DRAW', 'PLAYING'"""
        for x in range(self.dimx):
            row_win = True
            if self.grid[x][0] != '':
                for y in range(1, self.dimy):
                    if self.grid[x][y] != self.grid[x][0]:
                        row_win = False
                if row_win:
                    return 'WIN'                
            
        
        for y in range(self.dimy):
            row_win = True
            if self.grid[0][y] != '':
                for x in range(1, self.dimx):
                    if self.grid[x][y] != self.grid[0][y]:
                        row_win = False
                if row_win:
                    return 'WIN'        
                
        diag_win = True

        if self.grid[0][0] != '':
            for i in range(self.dimx):
                if self.grid[i][i] != self.grid[0][0]:
                    diag_win = False
        elif self.grid[self.dimx-1][0] != '':
            for i in range(self.dimx):
                if self.grid[i][self.dimy-1-i] != self.grid[self.dimx-1][0]:
                    diag_win = False
        else:
            diag_win = False
        
        if diag_win:
            return 'WIN'
        
        
        for col in self.grid:
            for value in col:
                if value == '':
                    return 'PLAYING'
        
        return 'DRAW'
        
    
    def reset(self):
        'resets the board'
        self.grid = []
        self.__init__()


    def print_grid(self):
        for y in range(self.dimy):
            line = ''
            for x in range(self.dimx):
                value = self.grid[x][y]
                if value == '':
                    value = '-'
                line += value + ' '
            print(line)
