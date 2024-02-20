import argparse
parser = argparse.ArgumentParser(description='calculator addition')
def add(x, y):
   return x+y
def subtract(x, y):
    return x-y

parser.add_argument("operation",  choices= ["add","subtract"])
parser.add_argument("x", type=float, help="The first number x")
parser.add_argument("y", type=float, help="The second number y")
args = parser.parse_args()
if args.operation == "add":
   result = add(args.x, args.y)
else:
   result = subtract(args.x, args.y)

print("Result:", result)