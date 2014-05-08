class Player(object):
    
    def __init__(self, name, piece):
        self.name = name
        self.piece = piece
        
    def get_move(self):
        valid = False
        while valid == False:
            valid = True
            row = int(input('{} what row do you want to place your {}?  '.
                            format(self.name, self.piece)))
            col = int(input('{} what column do you want to place your {} ?'.
                            format(self.name, self.piece)))
            if row > 2 or col > 2:
                print('{} your row or column must be a number between 0 and 2 inclusive'.
                      format(self.name, self.piece))
                valid = False
        return (row,col)
