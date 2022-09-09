#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

if len(argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
n1 = int(argv[1])
n2 = int(argv[3])
valid_op = ["+", "-", "*", "/"]
functions = [add, sub, mul, div]
for i, picker in enumerate(valid_op):
    if argv[2] == picker:
        print("{} {} {} = {}".format(n1, picker, n2, functions[i](n1, n2)))
        break
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
