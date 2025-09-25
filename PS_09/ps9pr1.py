# ps9pr1.py (Problem Set 9, Problem 1)
#
# A Connect Four Board class
#
# Computer Science 111
#

class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    ### add your constructor here ###
    #problem 1_1
    def __init__(self, height, width):
        """ constructs a new Board object by initializing the following three attributes.
        """
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]


    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''         #  begin with an empty string

        # add one row of slots at a time to s
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        ### add your code here ###
        #problem 1_2
        s += '-' * (2*self.width + 1)
        s += '\n'
        
        for i in range(self.width):
            s += ' ' + str(i % 10)
        
        s += '\n'
        
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        ### put the rest of the method here ###
        #problem1_3
        row = self.height -1
        
        while row >= 0 and self.slots[row][col] != ' ':
            row -= 1
            
        self.slots[row][col] = checker
        

    
    ### add your reset method here ###
    #problem 1_4
    def reset(self):
        """ reset the Board object on which it is called by setting all slots 
            to contain a space character.
        """
        #simplier way : using list comprehension!
        self.slots = [[' '] * self.width for row in range(self.height)]
        
        #more complex way: nested for loop:
        #for row in range(self.height):
        #    for col in range(self.width):
        #        self.slots[row][col] = ' '
    
   
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    ### add your remaining methods here
    #problem 1_6
    def can_add_to(self, col):
        """ returns True if it is valid to place a checker in the column col 
            on the calling Board object. Otherwise, it should return False.
        """
        if 0 <= col < self.width and self.slots[0][col] == ' ':
            return True
        else:
            return False
   
        
    #problem 1_7
    def is_full(self):
        """ returns True if the called Board object is completely full of checkers,
            and returns False otherwise.
        """
        for col in range(self.width):
            if self.can_add_to(col) == True:
                return False
        
        return True
    
    
    #problem 1_8
    def remove_checker(self, col):
        """ removes the top checker from column col of the called Board object.
            If the column is empty, then the method should do nothing.
        """
        for row in range(self.height):
            if self.slots[row][col] == 'X' or self.slots[row][col] == 'O' :
                self.slots[row][col] = ' '
                break
        
        #self.slots[row][col] = ' '
     
    #problem 1_9
    def is_win_for(self, checker):
        """ returns True if there are four consecutive slots containing checker
            on the board. Otherwise, it should return False.
        """
        assert(checker == 'X' or checker == 'O')
        
        def is_horizontal_win(self, checker):
            """ Checks for a horizontal win for the specified checker.
            """
            for row in range(self.height):
                for col in range(self.width - 3):
                    # Check if the next four columns in this row
                    # contain the specified checker.
                    if self.slots[row][col] == checker and \
                       self.slots[row][col + 1] == checker and \
                       self.slots[row][col + 2] == checker and \
                       self.slots[row][col + 3] == checker:
                        return True
        
            # if we make it here, there were no horizontal wins
            return False
        
        
        def is_vertical_win(self, checker):
            """ Checks for a vertical win for the specified checker.
            """
            for row in range(self.height - 3):
                for col in range(self.width):
                    # Check if the next four rows in this column
                    # contain the specified checker.
                    if self.slots[row][col] == checker and \
                       self.slots[row + 1][col] == checker and \
                       self.slots[row + 2][col] == checker and \
                       self.slots[row + 3][col] == checker:
                        return True

            # if we make it here, there were no horizontal wins
            return False
        
    
        def is_down_diagonal_win(self, checker):
            """ check for diagonals that go down from left to right
            """
            for row in range(self.height - 3):
                for col in range(self.width - 3):
                    # Check if the next four rows in this column
                    # contain the specified checker.
                    if self.slots[row][col] == checker and \
                       self.slots[row + 1][col + 1] == checker and \
                       self.slots[row + 2][col + 2] == checker and \
                       self.slots[row + 3][col + 3] == checker:
                        return True

            # if we make it here, there were no horizontal wins
            return False
        
        
        def is_up_diagonal_win(self, checker):
            """ check for diagonals that go up from left to right
            """
            for row in range(self.height - 3, self.height):
                for col in range(self.width - 3):
                    # Check if the next four rows in this column
                    # contain the specified checker.
                    if self.slots[row][col] == checker and \
                       self.slots[row - 1][col + 1] == checker and \
                       self.slots[row - 2][col + 2] == checker and \
                       self.slots[row - 3][col + 3] == checker:
                        return True

            # if we make it here, there were no horizontal wins
            return False
        
            
        if is_horizontal_win(self, checker) == True or \
           is_vertical_win(self, checker) == True or \
           is_down_diagonal_win(self, checker) == True or \
           is_up_diagonal_win(self, checker) == True:     
            return True
        else:
            return False
            
             
            