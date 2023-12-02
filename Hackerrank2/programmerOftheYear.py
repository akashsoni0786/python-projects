#!/bin/python3

import math
import os
import random
import re
import sys
def countX(lst, x):
    count = 0
    l =len(lst)
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count
def sockMerchant(n, ar):
    # Write your code here
    l=[]
    s = set(ar)
    print(s)
    d=list(s)
    d.sort()
    print(d)
    length = len(d)
    for i in range(0, length):
        a=countX(d,d[i])
        print(a)
        l.append(a)
    print(l)





n = int(input().strip())

ar = list(map(int, input().rstrip().split()))

result = sockMerchant(n, ar)

print(result)
