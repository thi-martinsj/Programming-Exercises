#!/bin/python3

import math
import os
import random
import re
import sys


def calculate_cost(s, target_magic_square):
    cost = 0
    for i in range(3):
        for j in range(3):
            dif = abs(s[i][j] - target_magic_square[i][j])
            cost += dif

    return cost

def formingMagicSquare(s):
    target_magic_squares = [
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
        [[8, 1, 6], [3, 5 ,7], [4, 9, 2]]
    ]

    final_cost = 99999999
    
    for target_magic_square in target_magic_squares:
        cost = calculate_cost(s, target_magic_square)

        if cost < final_cost:
            final_cost = cost
    
    return final_cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
