first_Number = int(input('Enter first number: '))
second_Number = int(input('Enter second number: '))
third_Number = int(input('Enter third number: '))
minimum = first_Number

if second_Number < first_Number:
     minimum = second_Number
if third_Number < minimum:
    minimum = third_Number

print(minimum)  