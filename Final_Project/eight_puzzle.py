#
# eight_puzzle.py (Final project)
#
# driver/test code for state-space search on Eight Puzzles   
#
# name: Sitong Yan
# email: sitongy2@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: Jun Wang
# partner's email: wangjun@bu.edu
#

from searcher import *
from timer import *

def create_searcher(algorithm, param):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * param - a parameter that can be used to specify either
            a depth limit or the name of a heuristic function
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(param)
    elif algorithm == 'BFS':
        searcher = BFSearcher(param)
    elif algorithm == 'DFS':
        searcher = DFSearcher(param)
    elif algorithm == 'Greedy':
        searcher = GreedySearcher(param)
    elif algorithm == 'A*':
        searcher = AStarSearcher(param)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher

def eight_puzzle(init_boardstr, algorithm, param):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * param - a parameter that is used to specify either a depth limit
            or the name of a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')
    searcher = create_searcher(algorithm, param)
    if searcher == None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()
    
    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()


def process_file(filename, algorithm, param):
    """ process the docstring to test different algorithm
    """
    file = open(filename, 'r')
    num_puzzles_solved = 0
    total_moves = 0
    total_states_tested = 0
    accumulation = 0
        
    for line in file:
        digit_str = line.strip('\n')
        b = Board(digit_str)
        s = State(b, None, 'init')
        searcher = create_searcher(algorithm, param)
        soln = None
        try:
            soln = searcher.find_solution(s)
            if soln is None:
                print(digit_str + ': no solution')
            else:
                num_puzzles_solved += 1
                total_moves = soln.num_moves 
                accumulation += total_moves
                total_states_tested += searcher.num_tested
                print(digit_str + ':', soln.num_moves, 'moves,', searcher.num_tested, 'states tested')
        except KeyboardInterrupt:
            print('search terminated, ', end='')
           
            
       
        if num_puzzles_solved > 0:
            avg_moves =  accumulation/ num_puzzles_solved
            avg_states_tested = total_states_tested / num_puzzles_solved
            print('\nsolved', num_puzzles_solved, 'puzzles')
            print('averages:', avg_moves, 'moves,', avg_states_tested, 'states tested')
        else:
            print('solved',0,'puzzles') 
            
