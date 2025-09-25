# ps7pr1.py - Problem Set 7, Problem 1
#
# String-method puzzles
#

s1 = 'Hickory Dickory Dock!'
s2 = 'The mouse ran up the clock.'

# Puzzle 0 (example)
answer0 = s2.lower().count('t')     

# Put your solutions to the remaining string puzzles below.
answer1 = s1.replace('ck', 'll')

answer2 = s2.split('e')

answer3 = s1.lower().split('ck')

answer4 = s1.upper().replace('D','H').replace('HICK','')

answer5 = s2.upper().split('E ')





# The code below tests the values of your expressions. DO NOT MODIFY IT!
if __name__ == '__main__':    
    for n in range(0, 6):
        answer_var = 'answer' + str(n)
        if answer_var in dir():
            print(answer_var, '=', eval(answer_var))
