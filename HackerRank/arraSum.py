def miniMaxSum(arr):
    # Write your code here
    l= len(arr)
    s1 = 0
    s2 = 0
    for i in range(0,l-1):
        s1+=arr[i]
    for j in range(1,l):
        s2+=arr[j]

    print(s1,s2)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(sorted(arr))

    # 396285104
    # 573261094
    # 759641832
    # 819230764
    # 364801279

    # 2093989309
    # 2548418794