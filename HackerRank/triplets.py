import numpy as np


class Triplet:
    def one(self,a, b):
        fl = 0
        sl = 0

        # a = []
        # b = []

        for i in range(0, 3):
            if a[i] > b[i]:
                fl += 1
            if a[i] < b[i]:
                sl += 1
            else:
                pass

        print(fl, sl)



n1 = input().split()
n2 = input().split()

# print(n1, n2)
a = []
b = []

for j in range(0, 3):
    q = int(n1[j])
    a.append(q)
    r = int(n2[j])
    b.append(r)
# print(a,b)
t=Triplet()

t.one(a, b)
