#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 16:58:04 2023

@author: yansitong
"""
#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    """ A subclass of Player
    """
    def __init__(self, checker, tiebreak, lookahead):
        """ construct a new AIPlayer object
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)

        super().__init__(checker)
        
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
    
    def __repr__(self):
        """ returns a string representing an AIPlayer object. 
        """
        s = ''
        checker_name = super().__repr__()
        s += checker_name + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'
        return s
    
    
    def max_score_column(self, scores) :
        """ returns the index of the column with the maximum score. 
        """
        max_score = max(scores)
        max_indices = [i for i, score in enumerate(scores) if score == max_score]
        
        if len(max_indices) == 1:
            return max_indices[0]

        if self.tiebreak == 'LEFT':
            return max_indices[0]
        if self.tiebreak == 'RIGHT':
            return max_indices[-1]
        if self.tiebreak == 'RANDOM':
            return random.choice(max_indices)
        
    
    def scores_for(self, b):
        """ return a list containing one score for each column.
        """
        scores = [50] * b.width
        
        for col in range(b.width):
            if not b.can_add_to(col):
                scores[col] = -1  # column is full
            elif b.is_win_for(self.checker):
                scores[col] = 100  # AIPlayer wins in this column
            elif b.is_win_for(self.opponent_checker()):
                scores[col] = 0  # opponent wins in this column
            elif self.lookahead == 0:
                scores[col] = 50  # no lookahead, so assume current board is neutral
            else:
                # Add checker to the board, create an opponent with one less lookahead, and determine their scores
                b.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opponent_scores = opponent.scores_for(b)

                # Determine the AIPlayer's score for this column based on the opponent's scores
                if max(opponent_scores) == 0:
                    scores[col] = 100  # this column leads to an immediate win
                elif 0 < max(opponent_scores) < 100:
                    scores[col] = 50  # this column doesn't lead to a loss or a win, so assume it's neutral
                else:
                    scores[col] = 0  # this column leads to a guaranteed loss

                b.remove_checker(col)  # remove checker to restore the board to its prior state

        return scores
    
    
    def next_move(self, b):
        """ this version of next_move should return the called AIPlayer‘s judgment 
        of its best possible move.
        """
        self.num_moves += 1
        scores = self.scores_for(b)
        return self.max_score_column(scores)
    
    