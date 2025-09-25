# function 1
def first_and_last(values):
    """ returns a new list containing the first value of the original list 
    followed by the last value of the original list 
    input values: a list contains any types of elements with undecided numbers
    """
    first = values[0]
    last = values[-1]
    return [first,last]


#function 2
def even_odd(s):
    """ returns a new string in which all of the characters that are in even 
    positions in the original string are followed by all characters in odd positions.
    input s: a random string
    """
    even = s[0: :2]
    odd = s[1: :2]
    return even + odd
    

#function 3
def move_to_end(s,n):
    """ returns the a new string in which the first n characters of s have 
    been moved to the end of the string.
    input s and n: a string value s and a non-negative integer n
    
    *special case: If n (the second input) is greater than or equal to the 
    length of s (the first input), then the function should simply return the 
    original s without changing it
    """
    if len(s) > n:
        s = s[n:] + s[0:n]
    return s


# test function with a sample test call for function 0
 # optional but encouraged: add test calls for your functions below
def test():
    """ performs test calls on the functions above """
    #function 1
    print("first_and_last([1,2,3,4]) returns", first_and_last([1,2,3,4]))
          
    #function 2
    print("even_odd('programming') returns", even_odd('programming'))
    
    #function 3
    print("move_to_end('computer',5) returns",move_to_end('computer',5))
    