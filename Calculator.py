import sys

def main():
    print(">>>Calculator with direct console input<<<")
    checkArguments()
    a = parseInput(1, sys.argv[1])
    rz = sys.argv[2]
    b = parseInput(3, sys.argv[3])
    erg = calculate(rz, a, b)
    printResult(a, b, rz, erg)

def checkArguments():
    if len(sys.argv) == 4:
        if not isValidComputeSign(sys.argv[2]):
            printError("rz")
    else:
        printError("arg")

def isValidComputeSign(rz):
    validSigns = {
        "+" : True,
        "-" : True,
        "*" : True,
        "/" : True
    }
    return validSigns.get(rz, False)

def parseInput(ind, num):
    try:
        out = float(num)
    except ValueError:
        out = float(0)
        print("A wild float conversion error occured! - The " + str(ind) + ". number was set to 0")
    finally:
        return out

def calculate(rz, a, b):
    calc = {
        "+" : a + b,
        "-" : a - b,
        "*" : a * b,
        "/" : a / b
    }
    return calc.get(rz)

def printResult(a, b, rz, erg):
    print("firstNumber: " + str(a))
    print("secondNumber: " + str(b))
    calcType = {
        "+" : "plus",
        "-" : "minus",
        "*" : "multiplied",
        "/" : "divided"
    }
    print("calculation type: " + calcType.get(rz))
    print("result: " + str(erg))

def printError(err):
    if err == "rz":
        print("Error! Please enter a valid compute sign as the second argument ... Shuting down the script!")
    if err == "arg":
        print("Error! Please enter three arguments ... Shuting down the script!")
    quit()

main()