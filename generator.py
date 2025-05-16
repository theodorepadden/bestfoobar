def checkFoo(num):
    if num % 5 == 0 and num != 0:
        return True
    else:
        return False

def checkBar(num):
    if num % 7 == 0 and num != 0:
        return True
    else:
        return False

top = int(input("Enter the number you want to go up to: "))
i = 0
while i <= top:
    returnString = ""
    temp = False
    if checkFoo(i):
        returnString += "Foo"
        temp = True
    if checkBar(i):
        returnString += "Bar"
        temp = True
    if temp is False:
        returnString += str(i)
    print(returnString)
    i += 1





