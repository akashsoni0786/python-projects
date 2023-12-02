from datetime import date
# Question 1
# names = ['Akash','Prince','Avi']
# ages = [10,20,30]
# salaries = [1000000,10000,1000]
#
# l = zip(names,ages,salaries)
# f=list(l)
# print(f)

# Question 2

# mat = [[1,2,3,3],[1,2,3,4],[1,2,3,4]]
# q = zip(*mat)
# lst = list(q)
# print(lst)

# Question 3

# x = [[1, 2, 3], [4, 5, 6]]
# y = [[11, 12], [21, 22],[31,32]]
#
# l1 = [xrow for xrow in x]
# print(l1)
#
# l2  = [(xrow,ycol) for ycol in zip(*y) for xrow in x]
# print(l2)
#
# l3 = [[sum(a*b for a,b in zip(xrow,ycol)) for ycol in zip(*y)] for xrow in x]
# print(l3)





# a = [[1,1,1],[1,1,1]]
# b= [[1,1],[2,2],[3,3]]
#
# li1 = [xrow for xrow in a]
# print(li1)
#
# li2 = [(xrow,ycol) for ycol in zip(*b) for xrow in a]
# print(li2)
#
# li3 = [[sum(a1*b1 for a1,b1 in zip(xrow,ycol)) for ycol in zip(*b)] for xrow in a]
# print(li3)

# Question4
# n= divmod(17,3)
# print(n)
#
# t=(17,3)
# s= divmod(*t)
# print(s)

#Question 5

# intgr = [1,2,3,4,5]
# flt= (1.1,2.2,3.3,4.4,5.5)
# zp = zip(intgr,flt)
# it = list(zp)
# print(it)
#
# for i,f in it:
#     print(i,f)

# Question 6

d1 =21
m1 = 2
y1 = 2020

d2 = 2
m2 = 3
y2 = 2021

dat1 =(y1,m1,d1)
dat2 =(y2,m2,d2)

# t1 = date(2021,12,21)
# t2 = date(2021,1,1)

t1 = date(dat1)
t2 = date(dat2)
t=(t1-t2).days

print("Date 1 :",dat1)

print("Date 2 :",dat2)

print(t)




#question 7

# items = (2,3,1,4,2,6,8,4,2)
# t= list(items)
# print(t)
# print(t.sort())


