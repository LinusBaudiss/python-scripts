import sys

def main():
    print(">>>Adding two numbers with direct console input<<<")
    checkArguments()
    a = parseInput(1, sys.argv[1])
    b = parseInput(2, sys.argv[2])
    sum = a + b
    printResult(a, b, sum)

def checkArguments():
    if len(sys.argv) == 3:
        continue    
    else:
        print("Error! Please enter two arguments ... Shuting down the script!")
        quit()

def parseInput(ind, num):
    try:
        out = float(num)
    except ValueError:
        out = float(0)
        print("A wild float conversion error occured! - The number with the index " + str(ind) + " was set to 0")
    finally:
        return out

def printResult(a, b, sum):
    print("firstNumber: " + str(a))
    print("secondNumber: " + str(b))
    print("sum: " + str(sum))

main()