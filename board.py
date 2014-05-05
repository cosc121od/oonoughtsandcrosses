'''The implementation of the board class'''
class Board(object):

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

                    
    