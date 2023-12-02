def staircase(n):
    for i in range(0,n):
        for j in range(0,n):
            print(" ")
        for k in range(0,n):
            print("*","\n")

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
