todaysDate = eval(input(
    "Enter an interger for today's day of the week from 0 - 6, Sunday is 0 and Saturday is 6.: "))


if todaysDate == 0:
    print("Today is Sunday")
elif todaysDate == 1:
    print("Today is Monday")
elif todaysDate == 2:
    print("Today is Tuesday")
elif todaysDate == 3:
    print("Today is Wednesday")
elif todaysDate == 4:
    print("Today is Thursday")
elif todaysDate == 5:
    print("Today is Friday")
elif todaysDate == 6:
    print("Today is Saturday")


daysElapsed = eval(input("Enter the number of days elapsed since today:"))

if daysElapsed == 1:
    print("Today is Sunday and the future day is Monday")
elif daysElapsed == 2:
    print("Today is Monday and the future day is tuesday")
else:
    if daysElapsed == 3:
        print("today is tuesday the next day is wednesday")
