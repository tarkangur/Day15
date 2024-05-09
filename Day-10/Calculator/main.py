from art import logo


def add (n1, n2):
  return n1 + n2

def subtract (n1, n2):
  return n1 - n2

def multiply (n1, n2):
  return n1 * n2

def divide (n1, n2):
  return n1 / n2

operations ={
  "+": add, 
  "-": subtract, 
  "*": multiply, 
  "/": divide             
}
def calculator():
  print(logo)
  num1 = float(input("What is your first number? "))
  for symbol in operations:
    print(symbol)
  calculate_con = True
  
  while calculate_con:
    operation_symbol = input("Pick another operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{answer} {operation_symbol} {num2} = {answer}")
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:. ") == "y":
      num1 = answer 
    else:
      calculate_con = False
      calculator()

calculator()
