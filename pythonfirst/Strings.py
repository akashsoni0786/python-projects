# Question 1

# msg1 = "Akash"
# msg2 = '''Akash
# kumar
# Soni'''
# msg3 = "Akash,Are you ok....She said,\"Something happens with you\""
# print(msg3)
# print(msg2)
# msg = msg2 + msg1
# print(msg)

# Question2

# s = "Bamboozled"
# print(s[0],s[1])
# print(s[-2],s[-1])
# print(s[2:])
# print(s[:-3])
# print(s)
# print(s[0::2])
# print(s[0::5])

# Question 3

# s1 = "NitiAayog"
# s2 = "And Quiet Flows The Don"
# s3 = "1234567890"
# s4 = "Make $1000 a day"
# print("Checking for S1 alphabet,alphanum,lower,upper")
# print(s1.isalpha())
# print(s1.isalnum())
# print(s1.islower())
# print(s1.isupper())
#
# print("Checking for S2 alphabet,alphanum,lower,upper")
# print(s2.isalpha())
# print(s2.isalnum())
# print(s2.islower())
# print(s2.isupper())
# print(s2.startswith('And', 0,))
# print(s2.endswith('And', -1,))
#
# print("Checking for S3 alphabet,alphanum,lower,upper")
# print(s3.isalpha())
# print(s3.isalnum())
# print(s3.islower())
# print(s3.isupper())
#
# print("Checking for S4 alphabet,alphanum,lower,upper")
# print(s4.isalpha())
# print(s4.isalnum())
# print(s4.islower())
# print(s4.isupper())
# print(s4.isnumeric())
# print(s4.isascii())
# print(s4.isupper())

# Question 4

# a = "Bring It On"
# print(a.upper())
# print(a.lower())
# print(a.capitalize())
# print(a.swapcase())
# print(a.replace("It", "Him"))
# print(a.find('It'))
# print(ord("a"))
#
# b = "    Flanked by spaces on either side             "
# print(b.lstrip())
# print(b.split())
# print(b.isspace())
# c =b.split()
# print(c.sort())
# print(c.append("OOO"))
# print(c.reverse())



# def rev(s):
#     if len(s)==0:
#         return s
#     else:
#         return rev(s[1:]) +s[0]
# s="AkashSoni"
# print(rev(s))


def rev(s):
    l = s[::-1]
    return l
s="Akash"
print(rev(s))