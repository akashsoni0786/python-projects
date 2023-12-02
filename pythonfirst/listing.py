# import keyword
#
# list1 = ['Anil','Anmol','Aditya','Avi','Alka']
# print(list1)
# list1.insert(1,"Anuj")
# print(list1)
# list1.append('Zulla')
# print(list1)
# list1.__delitem__(1)
# print(list1)
# del list1[3]
# print(list1)
# list1.sort()
# print(list1)
# list1.remove('Alka')
# print(list1)
# list1.insert(4,'Yogi')
# print(list1)
# print(keyword.kwlist)
# list1.pop()
# print(list1)
# print(list1.index('Zulla'))
# list1.reverse()
# print(list1)


# l1 = ['a','b','c',1,2,3]
# alp =[]
# num=[]
# l = len(l1)
#
# for i in range(l):
#
#     if l1[i].isalpha():
#         alp.append(l1[i])
#     else:
#         num.append(l1[i])
# print(alp)
# print(num)

if __name__ == '__main__':

    N = int(input("Enter number of commands \n"))
    print("Create list according to command")
    print("\'print\' for printing your list")
    print("\'append\' for appending in your list")
    print("\'insert\' for inserting your list")
    print("\'sort\' for sorting your list")
    print("\'pop\' for poping your list")
    print("\'reverse\' for reverse your list")
    print("\'remove\' for remove element from your list")


    l = []
    for i in range(0, N):


        s = input()

        # x, y = map(int, input().split())
        # print
        # append
        # insert
        # sort
        # pop
        # remove
        if s == "print":
            print(l)
        if s == "append":
            ap = input()
            l.append(ap)
        if s == "sort":
            l.sort()
        if s == "pop":
            l.pop()
        if s == "reverse":
            l.reverse()
        if s == "remove":
            rm = input()
            l.remove(rm)
        if s == "insert":
            pos = int(input())
            num = input()
            l.insert(pos, num)
    print(l)
