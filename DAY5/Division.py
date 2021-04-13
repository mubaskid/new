def Division(aList):
    for position in range(len(aList)):
        aList[position] =2 / aList[position]

numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 24, 26, 28, 30]
print(numbers)
Division(numbers)
print(numbers)

print()
