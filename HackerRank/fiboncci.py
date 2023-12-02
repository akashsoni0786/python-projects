n= int(input())

if n>0:
    if n==1:
        print(1)
    else:
        a = 0
        b = 1
        print(a)
        print(b)

        for i in range(0, n-2):
            c = a + b
            a = b
            b = c

            print(c)




