from art import logo

#Add function 
def add(n1, n2):
  total = n1 + n2
  return total

#subtract function 
def sub(n1, n2):
  total = n1 - n2
  return total 

#devide function 
def div(n1, n2):
  total = n1 / n2
  return total

#multiply function 
def mult(n1, n2):
  total = n1 * n2
  return total 

#dictionary of all operators a
calculator_dict = {
"+": add,
"-": sub,
"/": div,
"*": mult
}

def calculation():
  """
   Function that takes in 2 values and peforms an operaion on the numbers
   Add, subtract, multiply or devide
  """
  print(logo)
  num1 = float(input("What is the first number?: "))
  for opp in calculator_dict:
    print(opp)
    
  continue_cal = True 
  while continue_cal:
    operation_type = input("Pick an operation from the list above: ")
    num2 = float(input("What is the next number?: "))
    answer = calculator_dict[operation_type](num1, num2)
    print(f"{num1} {operation_type} {num2} = {answer}")
  
    if input("Do you want to go again, Type 'y' to continue and 'n' to start new.: ") == "y":
      num1 = answer
    else:
      continue_cal = False
      calculation()

calculation()
