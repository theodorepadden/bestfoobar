def checkFoo(num):
    if num % 5 == 0 and num != 0:
        return "Foo"
    else:
        return ""

def checkBar(num):
    if num % 7 == 0 and num != 0:
        return "Bar"
    else:
        return ""


def writeToMain(line):
    with open("main.py", "a") as f:
        f.write(line + "\n")


def setLargestNum(bigBoy = 1000):
    try:
        int(bigBoy)
        return bigBoy
    execpt:
        print("Input a integer (ex 1, 2, 3) Running with default (1000)")
        return 1000


#clears to make sure file is empty
with open("main.py", "w") as f:
    f.write("")

#todo add way to pass arg for amount of ints generated
largestNum = setLargestNum(input("Enter the larget num here: "))
writeToMain("i = 0")
writeToMain("while i < 100:")

currentNum = 0
while currentNum <= largestNum:
    line = "        print(\"" 
    writeToMain("   if i == " + str(currentNum) + ":")
    if checkFoo(currentNum) != "" or checkBar(currentNum) != "":
        line += checkFoo(currentNum)
        line += checkBar(currentNum)
    else:
        line += str(currentNum)
    writeToMain(line + "\")")
    currentNum += 1

writeToMain("   i += 1")



