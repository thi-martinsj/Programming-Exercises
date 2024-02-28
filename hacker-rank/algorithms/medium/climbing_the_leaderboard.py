#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    result = []
    scores = {}
    rank = 1
    temp_score = ranked[0]
    
    for score in ranked:
        if score != temp_score:
            rank += 1
            temp_score = score
        
        scores[score] = rank

    for score in player:
        left_ind = 0
        right_ind = ranked_count - 1

        while left_ind <= right_ind:
            ref_ind = (left_ind + right_ind) // 2
            if score == ranked[ref_ind]:
                result.append(scores[ranked[ref_ind]])
                break
            elif score < ranked[ref_ind]:
                left_ind = ref_ind + 1
            else:
                right_ind = ref_ind - 1
        else:
            if score > ranked[ref_ind]:
                result.append(scores[ranked[ref_ind]])
            else:
                result.append(scores[ranked[ref_ind]] + 1)
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
