import email.utils
import re
import math
import os
import random
import re
import sys

# regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
#
# n=int(input())
# for i in range(0,n):
#     x,y=map(str,input().split())
#     if bool(re.match(regex,y)):
#         print(email.utils.formataddr((x,y)).replace("<<","<").replace(">>",">"))
#
#
# # VIRUS <virus!@variable.:p>
#
#
# # print(email.utils.parseaddr('DOSHI <DOSHI@hackerrank.com>'))
# print(email.utils.formataddr(('DOSHI', 'DOSHI@hackerrank.com')))


# def comp(a,b):
#     la = len(a)
#     lb = len(b)
#     ca = 0
#     cb = 0
#     for i in range(0,la):
#         if a[i]>b[i]:
#             ca +=1
#         if a[i]<b[i]:
#             cb +=1
#     return a,b
#
# # if __name__ == '__main__':
#     # fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
# a = list(map(int, input().rstrip().split()))
#
# b = list(map(int, input().rstrip().split()))
#
# result = comp(a, b)
#
# print(' '.join(map(str, result)))
# print('\n')
#
# exit()

s = map(input())



print(s.capitalize())
print(s.upper())
