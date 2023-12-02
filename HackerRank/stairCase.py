n = int(input())

for i in range(1, n+2):
    for j in range(n+2, i, -1):
        print(" ",end="")
    for k in range(0, i):
        print("#",end="")
    print()
