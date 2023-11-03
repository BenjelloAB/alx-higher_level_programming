#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as calc

    a = sys.argv[:]
    e1 = int(a[1])
    e2 = int(a[3])
    if lena(a) == 1:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if a[2] == "+":
        print("{} {} {} = {:d}".format(a[1], a[2], a[3], calc.add(e1, e2)))
        sys.exit(0)
    elif a[2] == "-":
        print("{} {} {:d} = {:d}".format(a[1], a[2], a[3], calc.sub(e1, e2)))
        sys.exit(0)
    elif a[2] == "*":
        print("{} {} {} = {}".format(a[1], a[2], a[3], calc.mul(e1, e2)))
        sys.exit(0)
    elif a[2] == "/":
        print("{} {} {} = {}".format(a[1], a[2], a[3], calc.div(e1, e2)))
        sys.exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
