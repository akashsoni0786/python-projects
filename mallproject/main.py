l=[]
names=[]
moneyBybill=[]
def Name(nm):
    names.append(nm)

def totalMoney(m):
    moneyBybill.append(m)

def luckyWinner():
    le=len(names)
    x = max(moneyBybill)
    for i in range(0,le):
        if(moneyBybill[i]==x):
            print("Winner is ",names[i])






    


def productBill(a,b):
    l.append(a)
    sum = 0
    sum2 =0
    for i in range(len(l)):
        # print("i", i)
        # print(b)
        sum = sum + l[i]
        sum2 = sum2+b
    print("Now total number of items :", sum2)
    print("Total Calculate Bill :", sum)
    totalMoney(sum)

class Clothes():
    def shirt(self,n):
        count = n*200
        print("Total amount of shirt : ",count)
        productBill(count,n)
    def skirt(self,n):
        count = n*100
        print("Total amount of skirts : ",count)
        productBill(count,n)
    def pants(self,n):
        count = n*250
        print("Total amount of pants : ",count)
        productBill(count,n)
    def sarees(self,n):
        count = n*500
        print("Total amount of sarees : ",count)
        productBill(count,n)

class Jewellers():

    def Ring(self,n):
        count = n*200
        print("Total amount of Ring : ",count)
        productBill(count,n)

    def Nacklace(self,n):
        count = n*100
        print("Total amount of Nacklace : ",count)
        productBill(count,n)

    def Jhumka(self,n):
        count = n*250
        print("Total amount of Jhumka : ",count)
        productBill(count,n)

    def Diamonds(self,n):
        count = n*500
        print("Total amount of Diamonds : ",count)
        productBill(count,n)


class Footwear():

    def Nike(self,n):
        count = n*2000
        print("Total amount of shoes : ",count)
        productBill(count,n)

    def Paragon(self,n):
        count = n*100
        print("Total amount of shoes : ",count)
        productBill(count,n)

    def Spark(self,n):
        count = n*250
        print("Total amount of shoes : ",count)
        productBill(count,n)

    def Campus(self,n):
        count = n*500
        print("Total amount of shoes : ",count)
        productBill(count,n)

class Electronics():

    def LEDs(self,n):
        count = n*20000
        print("Total amount of LEDs : ",count)
        productBill(count,n)

    def Mobiles(self,n):
        count = n*10000
        print("Total amount of Mobiles : ",count)
        productBill(count,n)

    def Fridges(self,n):
        count = n*2500
        print("Total amount of Fridges : ",count)
        productBill(count,n)

    def Computers(self,n):
        count = n*50000
        print("Total amount of Computers : ",count)
        productBill(count,n)


class Mall(Clothes):

    def MallEntry(self):
        reply = int(input("Please enter 1 for enter inside"))
        print("====Welcome to Phoenix Mall====")
        print("For exit Please enter \n By ")

        while(1):
            nam = str(input("Enter your name :"))
            Name(nam)
            if(nam =="By"):
                exit()
            else:
                if (reply == 1):

                    while(1):
                        while (1):
                            print("1: Max Showroom \n2: Kalyan Jewellers\n3: Bata Showroom\n4: Relince Electronics")
                            n = int(input("Select your shop:\n"))
                            if (n == 1):
                                print("Welcome to Max Showroom\n")

                                while (1):
                                    print("1: Shirt Area\n2: Skirts\n3: Pants\n4: Sarees")
                                    a = int(input("Enter the number of the particular item :\n"))
                                    max = Clothes()
                                    if (a == 1):
                                        b = int(input("Enter the number of shirts :"))
                                        max.shirt(b)
                                        continue
                                    if (a == 2):
                                        b = int(input("Enter the number of skirts :"))
                                        max.skirt(b)
                                        continue
                                    if (a == 3):
                                        b = int(input("Enter the number of pants :"))
                                        max.pants(b)
                                        continue
                                    if (a == 4):
                                        b = int(input("Enter the number of sarees :"))
                                        max.sarees(b)
                                        continue
                                    else:
                                        print("Thanks for visiting Max")
                                        break
                            if (n == 2):
                                print("Welcome to Kalyan Jewellers\n")
                                while (1):
                                    print("1: Ring\n2: Necklace\n3: Jhumka\n4: Diamond Area")
                                    a = int(input("Enter the number of the particular item :\n"))
                                    kalyan = Jewellers()

                                    if (a == 1):
                                        b = int(input("Enter the number of Rings :"))
                                        kalyan.Ring(b)
                                        continue
                                    if (a == 2):
                                        b = int(input("Enter the number of Nacklace :"))
                                        kalyan.Nacklace(b)
                                        continue
                                    if (a == 3):
                                        b = int(input("Enter the number of Jhumka :"))
                                        kalyan.Jhumka(b)
                                        continue
                                    if (a == 4):
                                        b = int(input("Enter the number of Diamonds :"))
                                        kalyan.Diamond(b)
                                        continue
                                    else:
                                        print("Thanks for visiting Kalyan Jewellers")
                                        break
                            if (n == 3):
                                print("Welcome to Bata Showroom\n")
                                while (1):
                                    print("1: Nike\n2: Paragon\n3: Spark\n4: Compus")
                                    a = int(input("Enter the number of the particular item :\n"))
                                    bata = Footwear()

                                    if (a == 1):
                                        b = int(input("Enter the number of shoes :"))
                                        bata.Nike(b)
                                        continue
                                    if (a == 2):
                                        b = int(input("Enter the number of shoes :"))
                                        bata.Paragon(b)
                                        continue
                                    if (a == 3):
                                        b = int(input("Enter the number of shoes :"))
                                        bata.Spark(b)
                                        continue
                                    if (a == 4):
                                        b = int(input("Enter the number of shoes :"))
                                        bata.Campus(b)
                                        continue
                                    else:
                                        print("Thanks for visiting BATA")
                                        break
                            if (n == 4):
                                print("Welcome to Relience Digital\n")

                                while (1):
                                    print("1: LEDs\n2: Mobiles\n3: Fridges\n4: Computers")
                                    a = int(input("Enter the number of the particular item :\n"))
                                    rel = Electronics()
                                    if (a == 1):
                                        b = int(input("Enter the number of LEDs :"))
                                        rel.LEDs(b)
                                        continue
                                    if (a == 2):
                                        b = int(input("Enter the number of Mobiles :"))
                                        rel.Mobiles(b)
                                        continue
                                    if (a == 3):
                                        b = int(input("Enter the number of Fridges :"))
                                        rel.Fridges(b)
                                        continue
                                    if (a == 4):
                                        b = int(input("Enter the number of Computers :"))
                                        rel.Computers(b)
                                        continue
                                    else:
                                        print("Thanks for visiting Relience Digital")
                                        break
                            else:

                                print("Thanks for visiting Phoenix United Mall")

                                n = len(names)
                                for i in range(0, n):
                                    print(names[i], " : Rs ", moneyBybill[i])
                                # print(moneyBybill.sort())
                                luckyWinner()
                                break
                else:
                    print(names)
                    print("Thanks for visiting here")




m = Mall()
m.MallEntry()




