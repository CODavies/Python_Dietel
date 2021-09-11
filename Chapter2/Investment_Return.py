p = int(input("Enter your principal amount: "))
r = 0.07
n = int(input("Enter your number of years: "))
rate = (1 + r) ** n
a = p * rate
print("Your amount at the end of ", n, "years is: ", a)
