'''An OO implementation of the Noughts and Crosses game.
   Written for COSC121, 2013.
   Author: Richard Lobb
   Date: May 9, 2013.

   Modified May 8, 2014 to use  __getitem__
'''

from player import Player
from game import Game

if __name__ == '__main__':
    player1 = Player('Angus', 'O')
    player2 = Player('Zelda', 'X')
    Game(player1, player2).play()  # Construct a game and play it





