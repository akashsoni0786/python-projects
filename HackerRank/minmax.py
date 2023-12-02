
def miniMaxSum(arr):
    l=len(arr)
    s1 = 0
    s2 = 0
    for i in range(0, l-1):
        print(s1)
        s1 += arr[i]

    print("Second")
    for j in range(1, l):

        print(s2)
        s2 += arr[j]
    print(s1, s2)


arr = list(map(int, input().rstrip().split()))

miniMaxSum(arr)
