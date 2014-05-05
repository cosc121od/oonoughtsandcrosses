'''The implementation of the board class'''
class Board(object):
    dimx, dimy = 3
    grid = []
    for i in range(dimx):
        temp = []
        for j in range(dimy):
            temp.append('')
        grid.append(temp)
