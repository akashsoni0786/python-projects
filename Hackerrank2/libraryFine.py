#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import date


#
# Complete the 'libraryFine' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d1
#  2. INTEGER m1
#  3. INTEGER y1
#  4. INTEGER d2
#  5. INTEGER m2
#  6. INTEGER y2
#
def numOfDays(date1, date2):
    return (date2 - date1).days


def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    da = date(y1, m1, d1)
    db = date(y2, m2, d2)
    d = (da - db).days
    y = y1 - y2
    if y1 == y2 and m1==m2 and d1>d2:
        return abs(d*15)
    if y1==y2 and m1<m2 :
        return abs(m1-m2)*500
    if y1>y2:
        return 1000
    else:
        return 0



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    d1 = int(first_multiple_input[0])

    m1 = int(first_multiple_input[1])

    y1 = int(first_multiple_input[2])

    second_multiple_input = input().rstrip().split()

    d2 = int(second_multiple_input[0])

    m2 = int(second_multiple_input[1])

    y2 = int(second_multiple_input[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()
