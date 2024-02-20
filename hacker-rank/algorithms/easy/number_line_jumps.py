#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    dif_initial_pos = (x2 - x1) if x2 >= x1 else (x1 - x2)
    dif_jump = (v1 - v2) if x2 >= x1 else (v2 - v1)

    if dif_jump == 0 and dif_initial_pos == 0:
        pos = 0
        rest = 0
    elif dif_jump == 0 and dif_initial_pos != 0:
        pos = -1
        rest = -1
    else:
        pos = dif_initial_pos / dif_jump
        rest = dif_initial_pos % dif_jump

    if pos < 0 or rest != 0:
        return "NO"
    
    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
