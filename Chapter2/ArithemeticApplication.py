print('Enter two integers and i will tell you their the relationship they satisfy')
first_Number = int(input('Enter first number: '))
second_Number = int(input('Enter second number: '))
if first_Number == second_Number:
    print(first_Number, 'is equal to', second_Number)
if first_Number != second_Number:
    print(first_Number, 'is not equal to', second_Number)
if first_Number < second_Number:
    print(first_Number, 'is less than ', second_Number)
if first_Number > second_Number:
    print(first_Number, 'is greater than ', second_Number)
if first_Number <= second_Number:
    print(first_Number, "is less than or equal ", second_Number)
if first_Number >= second_Number:
    print(first_Number, 'is greater than or equal ', second_Number)
