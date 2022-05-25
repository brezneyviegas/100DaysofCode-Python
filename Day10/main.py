[200~from art import logo
print(logo)



def add(n1, n2):
  total = n1 + n2
  return total

def sub(n1, n2):
  total = n1 - n2
  return total 

def div(n1, n2):
  total = n1 / n2
  return total

def mult(n1, n2):
  total = n1 * n2
  return total 

calculator_dict = {
"+": add,
"-": sub,
"/": div,
"*": mult
}

def calculation():
  num1 = float(input("What is the first number?: "))
  for opp in calculator_dict:
    print(opp)
    
  exit_cal = False 
  while not exit_cal:
    operation_type = input("Pick an operation from the list above: ")
    num2 = float(input("What is the next number?: "))
    answer = calculator_dict[operation_type](num1, num2)
    print(f"{num1} {operation_type} {num2} = {answer}")
  
    if input("Do you want to go again, Type 'y' to continue and 'n' to start new.: ") == "y":
      num1 = answer
    else:
      exit_cal = True
      calculation()

calculation()
