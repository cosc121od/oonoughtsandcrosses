'''The main OO noughts and crosses player.
   Simply imports the required classes and plays one game.'''

from game import Game
from board import Board
from player import Player

def main():
    '''The main function. Every home should have one'''
    player1 = Player('Angus', 'X')
    player2 = Player('Zelda', 'O')
    Game(player1, player2).play()

main()
