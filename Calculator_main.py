from art import logo
print(logo)

def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2
  
operators={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}

def calculator():
  num1=float(input("What's the first number?: "))
  for symbol in operators:
     print(symbol)
    
  for_calculation=True
  while for_calculation:
    operators_symbol=input("Pick an operation from the line above: ")
    num2=float(input("What's the second number?: "))
    calculation_function=operators[operators_symbol]
    answer=calculation_function(num1,num2)
  
    print(f"{num1} {operators_symbol} {num2} = {answer}")
  
    if input(f"Type 'y' to continue calclating with {answer}, or type 'n' to start new calculation.: ")=="y":
      num1=answer
    else:
      for_calculation=False
      calculator()

calculator()