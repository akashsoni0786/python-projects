
import math
import random
# x = int(input("Enter value of x \n"))
# y = int(input("Enter value of y \n"))


# print("Before Swaping :")
# print("x = ",x," y = ",y)
#
# x , y = y , x
# print("After Swaping :")
#
#
# print("x = ",x," y = ",y)   # Question1


# print(int(math.sqrt(pow(x,2)+pow(y,2))))  #Quertion2
#
# a= random.randint(10,50)
# b= random.randint(10,50)
#
# c= random.randint(10,50)
#
# d= random.randint(10,50)
# e= random.randint(10,50)
#
# print(random.seed(6,a))
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)     #Question3





# #Question4
#
# n= float(input("Enter number"))
#
# print("Trunc :")
# print(math.trunc(n))
# print("Ceil :")
# print(math.ceil(n))
# print("Floor :")
# print(math.floor(n))
# print("Round :")
# print(round(n))

#Question5

# salary = random.randint(15000,18000)
# print("Salary : ",salary,"\n")
#
# resultantSalary = salary-((salary*(.4)+salary*(.2)))
#
# print("Gross salary :",resultantSalary)

#Question6

# distanceBtwCities = int(random.randint(1,5))
# print("Distance in Kms : ",distanceBtwCities)
# print("Distance in meters :" ,distanceBtwCities*1000,"Meters")
# print("Distance in feet :",distanceBtwCities*(3280.1),"Feet")
# print("Distance in inches :",distanceBtwCities*39370,"Inches")
# print("Distance in centimeters :",distanceBtwCities*100000,"Centimeters")


#Question7

# print("Imaginary part of 2+3j  :",(2+3j).imag)
# print("Real part of 2+3j  :",(2+3j).real)
# print("Conjugate of 2+3j  :",(2+3j).conjugate())



#String Chapter 2

# a1 = '''how
#             are
#                     you?'''
#
# print(a1.isalnum())
# print(a1.isascii())
# print(a1.find("you"))
# print(a1.capitalize())
# print(a1.isalpha())
# print(a1.islower())
# print(a1.isupper())




# print(round(15.36))


# n = int(input())
#
# i = bin(n)
# j = i.replace("0b", "")
# m = str(j)
# l = j.__len__
# a = 0
# for k in range(0, l):
#     if (m[k] == m[k + 1]):
#         a=a+1
#
# print(a)


# Enter your code here. Read input from STDIN. Print output to STDOUT


# n = int(input())
# yupp = False
# for i in range(0, n):
#     num = int(input())
#     if num == 1:
#         print("Prime")
#
#     if num > 1:
#         for j in range(2, num):
#             if num % j == 0:
#                 yupp = False
#                 break
#             else:
#                 yupp = True
#
#         if yupp == False:
#             print("Not prime")
#         else:
#             print("Prime")


n= int(input())
s = '00'+str(n)
ad3 = int(s[-1])+int(s[-2])+int(s[-3])
ad4 = int(s[-1])+int(s[-2])
if n==1:
    print("Prime")
elif n%2==0:
    print("Not prime")
elif ad3%3==0:
    print("Not prime")
elif ad4%4==0:
    print("4")
    print("Not prime")
elif int(s[-1])==5:
    print('5')
    print("Not prime")
elif ad3%8 ==0:
    print('8')
    print("Not prime")
else:
    print("Prime")
