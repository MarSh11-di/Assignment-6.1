import argparse
parser = argparse.ArgumentParser(description='calculator addition')
def add(x, y):
   return x+y
def subtract(x, y):
   return x-y
def division(x,y):
   if y == 0:
      print("You cannot divide by 0") 
      exit()
   return round((x/y),2)


parser.add_argument("operation",  choices= ["add","subtract","division"])
parser.add_argument("x", type=float, help="The first number x")
parser.add_argument("y", type=float, help="The second number y")
args = parser.parse_args()
if args.operation == "add":
   result = add(args.x, args.y)
elif args.operation == "subtract":
   result = subtract(args.x, args.y)
elif args.operation == "division":
   result = division(args.x, args.y)

print("Result:", result)