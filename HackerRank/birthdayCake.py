import os


def birthdayCakeCandles(candles):
    l = len(candles)
    sum=1
    # print(candles)
    for i in  range(0,l-1):
        # print(candles[l-1])

        if candles[l - 1]==candles[i]:

            sum+=1

    print(sum)




candles_count = int(input().strip())

candles = list(map(int, input().rstrip().split()))

birthdayCakeCandles(sorted(candles))


