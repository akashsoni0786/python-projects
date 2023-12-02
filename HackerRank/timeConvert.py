def timeConversion(s):
    l = len(s)
    a=""

    t1 = s[0]
    t2 = s[1]
    t = int(t1 + t2)

    if s[8] == "P":
        if t < 12:
            a = str(t + 12)
            # print(a)
        if t == 12:
            a = "12"
            # print(a)
        print(a,end="")
        print(s[2], end="")
        print(s[3], end="")
        print(s[4], end="")
        print(s[5], end="")
        print(s[6], end="")
        print(s[7], end="")
    if s[8] == "A"and t!=12:
        for i in range(0,8):
            print(s[i],end="")
    if s[8] == "A" and t==12:
        a = "00"
        # print(a)
        print(a, end="")
        print(s[2], end="")
        print(s[3], end="")
        print(s[4], end="")
        print(s[5], end="")
        print(s[6], end="")
        print(s[7], end="")






s = input()
# print(s)

timeConversion(s)
