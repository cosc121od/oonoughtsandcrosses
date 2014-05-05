'''The implementation of the board class'''
class Board(object):
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
