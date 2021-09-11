first_Number = int(input('Enter first number: '))
second_Number = int(input('Enter second number: '))

if second_Number % first_Number == 0:
    print(first_Number, " is a multiple of ", second_Number)
if second_Number % first_Number != 0:
    print("The are not multiples")