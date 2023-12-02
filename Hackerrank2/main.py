#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np


#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here
    li=[]
    le=len(li)
    sum = 0
    for i in range(0, n):
        for j in range(0, n):
            if ar[i] != ar[j]:
                li.append(ar[i])
                if (ar[i] + ar[j]) % k == 0:
                    # print(ar[i] , ar[j])
                    for l in range(0,le):
                        if ar[i] != li[l]:
                            sum += 1
                    break
    return sum




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

ar = list(map(int, input().rstrip().split()))

result = divisibleSumPairs(n, k, ar)
print(result)


