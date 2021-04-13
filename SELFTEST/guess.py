import random


number = random.randint(0, 100)

for i in range(1, 99):
    try:
        user = int(input("Guess the lucky number: "))
        if user == number:
            print("Hurray!!")
            print(f"You guessed the number right, it's {number}")
            break

    except(ValueError):
        user != number
        print(f"Your Guess is Incorrect, the number is {number}")