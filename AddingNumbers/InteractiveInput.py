def main():
    print(">>>Adding two numbers with interactive console input<<<")
    a = getConsoleInput("first Number")
    b = getConsoleInput("second Number")
    sum = a + b
    printResult(a, b, sum)

def getConsoleInput(x):
    try:    
        out = float(input("Please enter the value for the " + x + ": "))
    except ValueError:
        out = float(0)
        print("A wild float conversion error occured! - The " + x + " was set to 0")
    finally:
        return out

def printResult(a, b, sum):
    print("firstNumber: " + str(a))
    print("secondNumber: " + str(b))
    print("sum: " + str(sum))

main()