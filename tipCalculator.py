#Tip Calculator

print("Welcome to the tip calculator")
total_Bill = float(input("What was the total bill?  $"))
tip_Percentage = int(input("How Much tip would you like to give?  12, 15 or custom? "))
splitting_bill = int(input("How Many people are splitting the bill?"))
outcome = ((total_Bill*(tip_Percentage / 100) + total_Bill)) /splitting_bill
print(f"Each person should pay: ${round(outcome,2)}")
