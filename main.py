def add(n1, n2):
  """adds one number to another"""
  return n1 + n2

def subtract(n1, n2):
  """subtracts one number from another"""
  return n1 - n2

def multiply(n1, n2):
  """multiplies one number with another"""
  return n1 * n2

def divide(n1, n2):
  """divides one number by another"""
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  from art import logo
  print(logo)
  num1 = float(input("What's the first number? "))
  for symbol in operations:
    print(symbol)

  continue_with_calculator = True

  while continue_with_calculator:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number? "))
    answer = (operations[operation_symbol](num1, num2)) 

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start again: ") == "y":
      num1 = answer
    else:
      continue_with_calculator = False
      calculator()
calculator()