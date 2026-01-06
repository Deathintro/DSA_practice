#Tip calculator
print("Welcome to the tip calculator!")
tot_bill = float(input("What was the total bill? $"))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15?"))
no_of_people = int(input("How many people to split the bill?"))
tip_pay = tot_bill * (tip_percent / 100)
each_person_share =  round(((tot_bill + tip_pay) / no_of_people), 2)
print(f"Each person should pay: ${each_person_share}")