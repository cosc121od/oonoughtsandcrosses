'''The implementation of the board class'''
class Board(object):
<<<<<<< HEAD

    def __init__(self):
        self.dimx = 3
        self.dimy = 3
        self.grid = []
        for i in range(self.dimx):
            temp = []
            for j in range(self.dimy):
                temp.append(' ')
            self.grid.append(temp)
    
    
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

                    
    
=======
    dimx, dimy = 3, 3
    grid = []
    #first dimention are the rows, second is each of the data values inside each row
    
    def __init__(self):
        'initiates the Board class'
        for i in range(dimx):
            temp = []
            for j in range(dimy):
                temp.append('')
            grid.append(temp)
    
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
    
    def is_triple(self, xytuple):
        'returns true if there is a triple intersecting x,y. To be used after set_point'
        pass
    
    def reset(self):
        'resets the board'
        self.grid = []
        self.__init__()
>>>>>>> 2a84e735db85bdd60d77144f54fcd59d23c75e35
