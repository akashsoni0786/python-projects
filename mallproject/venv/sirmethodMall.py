l =[]

def productBill(a):
    l.append(a)
    sum = 0
    for i in range(len(l)):
        print("i", i)
        print("l[i]", l[i])
        sum = sum + l[i]
    print("Calculate Bill", sum)
class Clothes() :
    def clothesMenu(self):
        print("============================ Welcome To Divyansh Mall Clothes Shop ===============================")
        print("============================ Please Choose Any One ===============================")
        print(" 1:shirts \n  2:pants \n  3: skirts \n 4:sarees \n 5:exit")
        a = int(input("Please Choose "))
        if (a == 1):
            shirtPrice = 300
            qty = int(input("how many shirts you want to purchase"))
            t = qty * shirtPrice
            productBill(t)
            # print(l)
            c = Clothes()
            c.clothesMenu()
        elif (a == 2):
            pantPrice = 800
            print("pants")
        elif (a == 3):
            skirtsprice = 600
            print("skirts")
        elif (a == 4):
            sareesprice = 1000
            print("sarees")

        elif (a == 5):
            main = Mall()
            main.mallMain()
class Jewellery():
    def jwelleryMenu(self):
        print("============================ Welcome To Divyansh Mall Jwellery Shop ===============================")
        print("============================ Please Choose Any One ===============================")
        print(" 1:Neckless \n  2:Kangan \n  3: exit")
        a = int(input("Please Choose "))
        if (a == 1):
            print("Neckless")
        elif (a == 2):
            print("Kangan")

        elif (a == 3):
            main = Mall()
            main.mallMain()

class Footwear():
    def footwearMenu(self):
        print("============================ Welcome To Divyansh Mall Footwear Shop ===============================")
        print("============================ Please Choose Any One ===============================")
        print(" 1:shoes \n  2:slippers \n  3: exit")
        a = int(input("Please Choose "))
        if (a == 1):
            print("shoes")
        elif (a == 2):
            print("slippers")

        elif (a == 3):
            main = Mall()
            main.mallMain()
class Electronics():
    def electronicsMenu(self):
        print("============================ Welcome To Divyansh Mall Electronics Shop ===============================")
        print("============================ Please Choose Any One ===============================")
        print(" 1:TV \n  2:mobiles \n 3: Refrigerator \n 4:washing machine \n 5: exit")
        a = int(input("Please Choose "))
        if (a == 1):
            print("TV")
        elif (a == 2):
            print("mobiles")
        elif (a == 3):
            print("Refrigerator")
        elif (a == 4):
            print("washing machine")
        elif (a == 5):
            main = Mall()
            main.mallMain()


class Mall:

    def mallMain(self):
        print("============================ Welcome To Divyansh Mall ===============================")
        print("============================ Please Choose Any One ===============================")
        print(" 1:Clothes \n  2:Jwellery \n  3:Footwear \n 4:Electronics ")
        a = int(input("Please Choose "))
        if(a == 1):
           # print("Clothes")
           c = Clothes()
           c.clothesMenu()
        elif(a == 2):
            # print("Jwellery")
            j = Jewellery()
            j.jwelleryMenu()

        elif(a == 3):
            #print("Footwear")
            f = Footwear()
            f.footwearMenu()
        elif(a == 4):
            #print("electronics")
            e = Electronics()
            e.electronicsMenu()
        # elif (a == 5):
        #     print('BILL')
        #     totalBill(t)
        else:
            print("Please Choose between 1-4")



m = Mall()
m.mallMain()
