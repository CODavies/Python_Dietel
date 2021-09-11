weightInPounds = int(input("Enter your weight in pounds: "))
heightInInches = int(input("Enter your height in inches: "))
BMI_Calculator = weightInPounds * 703 / (heightInInches * heightInInches)
print(BMI_Calculator)
if BMI_Calculator < 18.5:
    print("You are under weight")
if 18.5 < BMI_Calculator < 24.9:
    print("You are normally weight")
if BMI_Calculator > 25:
    print("You are obese")