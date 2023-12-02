
class Laundary:
    def __init__(self,id,name,n,price=0,tax=0):
        self.id = id
        self.name = name
        self.n =n
        self.price = price
        self.tax = tax

    def display_cloth_details(self):
        print("Name : ",self.name,"1 Id: ",self.id)
        print("Total no of clothes: ",self.n)
    def onlyPrice(self):
        self.price = self.n * 100
        return self.price

    def GST(self):
        a = int(self.onlyPrice())
        self.tax = a*(0.18)
        return self.tax
    def calculate_bill(self):
        a =int(self.onlyPrice())
        b=self.GST()
        print("Clothes price:",a)
        print("Total tax: ",b)
    def generateBill(self):
        a = int(self.onlyPrice())
        b = int(self.GST())
        print("Clothes price:", a)
        print("Total tax: ", b)
        print("Total Price : ", a + b)

id = input("Enter Id : ")
name = input("Enter name : ")
n = int(input("Enter total no. of clothes : "))

obj = Laundary(id,name,n)
obj.display_cloth_details()
obj.calculate_bill()
obj.generateBill()
