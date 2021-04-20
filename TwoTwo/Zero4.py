num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Enter which operation would you like to perform?")
x = input("Enter any of these for specific operation addition,subtraction,multiplication,division: ")

result = 0
if x == 'addition':
    result = num1 + num2
elif x == 'subtraction':
    result = num1 - num2
elif x == 'multiplication':
    result = num1 * num2
elif x == 'division':
    result = num1 / num2
else:
    print("Input character is not recognized!")

print(num1, x, num2, ":", result)
