#
# a= {1,2,3,3,3,4,4,4}
# b={1,2,2,2,3,3,4,5}
#
# print(a-b)
# print(b-a)
# print(a & b)
# print(a | b)
# print(a^b)

n = int(input())

for i in range(0, n):
    s = input()
    if s.isnumeric() and len(s) == 10:
        if s[0] == '7' or s[0] == '8' or s[0] == '9':
            print("YES")
    if s.isnumeric() and len(s) == 10:
        if s[0] == '1' or s[0] == '2' or s[0] == '3' or s[0] == '4' or s[0] == '5' or s[0] == '6':
            print("NO")


    else:
        print("NO")
exit()
