#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxSubarrayValue' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarrayValue(arr):
    # Write your code here
    l = len(arr)
    lip = []
    lp = 0
    lin = []
    ln = 0

    for i in range(0, l):
        if arr[i] > 0:
            lip.append(arr[i])
            lp += arr[i]
        if arr[i] < 0:
            print(arr[i])
            lin.append(arr[i])
            ln += arr[i]

    l1 = len(lip)
    l2 = len(lin)
    lip.sort()
    lin.sort()
    print(lip[l1-1])
    print(lin[0])

    # r = (lp - ln) * (lp - ln)
    r = (lip[l1-1]-lin[0])*(lip[l1-1]-lin[0])
    return r



arr_count = int(input().strip())

arr = []

for _ in range(arr_count):
    arr_item = int(input().strip())
    arr.append(arr_item)

result = maxSubarrayValue(arr)

print(str(result))
