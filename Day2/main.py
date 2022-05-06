#Get values to cal
print("Welcome to Tip Calculator!")
total_bill = input("What was the total bill?\n £")
tip_given = input("How much tip would you like to give? 10, 12, or 15?\n")
num_people = input("How many people to split the bill?\n")

#Convert user input to decimal numbers
new_total_bill = float(total_bill)
new_tip_given = float(tip_given)
new_num_people = float(num_people)

#calculate the total bill
total = (new_total_bill / new_num_people) * (new_tip_given * .01 + 1)

#Print out the total rounding to 2 decimal places
print(f"Each person should pay: £{round(total, 2)}")
