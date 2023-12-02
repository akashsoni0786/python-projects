if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    a = list(arr)
    a.sort()
    for i in range(0, n):
        if a[i] == a[n - 1]:
            print(a[i - 1])
            break
