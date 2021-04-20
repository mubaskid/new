import random


number = random.randint(0, 100)

for i in range(1, 99):
    try:
        user = int(input("Guess the lucky number: "))
        if user == number:
            print("Hurray!!")
            print(f"Your price 10,000$ and the number is {number}")
            break

    except(ValueError):
        user != number
        print(f"Your Guess is Incorrect, your price is 3,000$ and the number is {number}")
        
        #i don't know why its not running as expected"""
