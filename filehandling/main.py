# f = open("Akash.txt","r")
# f.write("hello This is akash\n")
# f.write("hello This is prince\n")
# f.write("hello This is dev\n")
# f.write("hello This is shailendra")
# f.readlines()
# f.close()
#
# f2 = open("Akash2.txt","a")
# f2.write("hello This is prince\n")
# f2.write("hello This is dev\n")
# f2.write("hello This is shailendra")
# f2.close()

f3 = open("Akash2.txt","r")
data  = f3.readlines()
print(data[0])
f3.close()