#
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below.

class Player:
    """ represent a player of the Connect Four game
    """
    
    def __init__(self, checker):
        """ constructs a new Player object by initializing the following two attributes.
        """
        assert(checker == 'X' or checker == 'O')
        
        self.checker = checker
        self.num_moves = 0
        
        
    def __repr__(self):
        """ returns a string representing a Player object. The string returned 
            should indicate which checker the Player object is using. 
        """
        s = 'Player' + ' ' + self.checker
        return s
         

    def opponent_checker(self):
        """ returns a one-character string representing the checker of the 
            Player object’s opponent.
        """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
        

    def next_move(self, b):
        """ returns the column where the player wants to make the next move.
        """
        col_num = int(input('Enter a column: '))
        
        
        while b.can_add_to(col_num) == False:
            print("Try again !")
            col_num = int(input('Enter a column: '))
        
        self.num_moves += 1
        return col_num
    
    