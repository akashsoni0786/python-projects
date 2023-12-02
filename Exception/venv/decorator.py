def hellohii(func):
    def inner():
        print("hiii",end=" ")
        return func
    return inner()

@hellohii
def name():
    print("Divyansh")

name()