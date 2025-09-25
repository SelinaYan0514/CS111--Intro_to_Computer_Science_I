# ps3pr3.py (Problem Set 3, Problem 3)
#
# Caesar cipher / decipher


#funtion 1
# A template for the first function that you are required to write.
def rotate(c, n):
    """ returns a single character that is based on c. If c is a letter of the
    alphabet, the function should “rotate” it by n characters forward in the 
    alphabet, wrapping around as needed.
        inputs c and n: a single character c and a non-negative integer n 
    between 0 and 25
    """
    # check to ensure that c is a single character
    assert(type(c) == str and len(c) == 1)

    # Put the rest of your code for this function below.
    if 'a' <= c <= 'z':
        new_word = ord(c) + n
        if new_word > ord('z'):
           new_word = new_word - 26
    elif 'A' <= c <= 'Z':
        new_word = ord(c) + n
        if new_word > ord('Z'):
           new_word = new_word - 26
    else:
        new_word = ord(c)
    return chr(new_word)


#function 2
#### Put your code for the encipher function below. ####
def encipher(s, n):
    """return a new string in which the letters in s have been “rotated” by n 
    characters forward in the alphabet, wrapping around as needed
        inputs s and n:  an arbitrary string s and a non-negative integer n 
    between 0 and 25
    """
    if s == '':
        return ''
    else:
        encipher_rest = encipher(s[1:], n)
        return rotate(s[0], n) + encipher_rest
    
    
# A helper function that you will use in implementing your 
# string_score function.
# You should *NOT* modify this function.
def letter_score(c):
    """ takes a single character c and returns a numeric score that 
        is based on how frequently that character appears in 
        English-language text documents.
        adapted from:
        http://www.cs.chalmers.se/Cs/Grundutb/Kurser/krypto/en_stat.html
    """
    # check to ensure that c is a single character
    assert(type(c) == str and len(c) == 1)

    if c == ' ': 
        return 0.1904
    elif c == 'e' or c == 'E': 
        return 0.1017
    elif c == 't' or c == 'T': 
        return 0.0737
    elif c == 'a' or c == 'A': 
        return 0.0661
    elif c == 'o' or c == 'O': 
        return 0.0610
    elif c == 'i' or c == 'I': 
        return 0.0562
    elif c == 'n' or c == 'N': 
        return 0.0557
    elif c == 'h' or c == 'H': 
        return 0.0542
    elif c == 's' or c == 'S': 
        return 0.0508
    elif c == 'r' or c == 'R': 
        return 0.0458
    elif c == 'd' or c == 'D': 
        return 0.0369
    elif c == 'l' or c == 'L': 
        return 0.0325
    elif c == 'u' or c == 'U': 
        return 0.0228
    elif c == 'm' or c == 'M': 
        return 0.0205
    elif c == 'c' or c == 'C': 
        return 0.0192
    elif c == 'w' or c == 'W': 
        return 0.0190
    elif c == 'f' or c == 'F': 
        return 0.0175
    elif c == 'y' or c == 'Y': 
        return 0.0165
    elif c == 'g' or c == 'G': 
        return 0.0161
    elif c == 'p' or c == 'P': 
        return 0.0131
    elif c == 'b' or c == 'B': 
        return 0.0115
    elif c == 'v' or c == 'V': 
        return 0.0088
    elif c == 'k' or c == 'K': 
        return 0.0066
    elif c == 'x' or c == 'X': 
        return 0.0014
    elif c == 'j' or c == 'J': 
        return 0.0008
    elif c == 'q' or c == 'Q': 
        return 0.0008
    elif c == 'z' or c == 'Z': 
        return 0.0005
    else:
        return 0.0


#### Put your code for string_score and decipher below. ####
#function 4
def  string_score(s):
    """ return the sum of the letter-score values of the characters in s
        input s: an arbitrary string s
    """
    return sum([letter_score(char) for char in s])


#function 5
def decipher(s):
    """ return to the best of its ability, the original English string, 
    which will be some rotation (possibly 0) of the input string s
        input s: an arbitrary string s
    """
    options = [encipher(s, n) for n in range(26)]
    scores = [[string_score(x), x] for x in options]
    bestpair = max(scores)
    return bestpair[1]


# test function with a sample test call for function 0
def test():
    """ performs test calls on the functions above """
    #function 1
    print("rotate('y', 5) returns", rotate('y', 5))
    
    #function 2
    print("encipher('#caesar!', 2) returns", encipher('#caesar!', 2))
    
    #function 4
    print("string_score('brutus') returns", string_score('brutus'))
    
    #function 5
    print("decipher('kwvozibctibqwva izm qv wzlmz nwz iv mfkmttmvb rwj') returns",
          decipher("kwvozibctibqwva izm qv wzlmz nwz iv mfkmttmvb rwj"))
    