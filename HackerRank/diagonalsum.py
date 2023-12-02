import os
import math


def diagonalDifference(arr, n):
    l1 = []
    l2 = []

    for i in range(0, n):
        for j in range(0, n):

            if i == j:
                l1.append(arr[i][j])
            if (i + j) == (n - 1):
                l2.append(arr[i][j])

    l3 = len(l1)
    # l4 = len(l2)
    suml=0
    sumr=0
    for k in range(l3):
        suml+=l1[k]
        sumr+=l2[k]
    return abs(suml - sumr)




# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr, n)
print(result)

# fptr.write(str(result) + '\n')
#
# fptr.close()
