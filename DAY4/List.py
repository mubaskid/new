NUMBERS = 6
numbers = []
sum = 0


for i in range(NUMBERS):
    value = int(input("Enter a number: "))
    numbers.append(value)
    sum += value


average = sum / NUMBERS

count = 0
for i in range(NUMBERS):
    if numbers[i] > average:
        count += 1

print("average is", average)
print("number above average is", count)