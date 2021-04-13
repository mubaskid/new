# from typing import Counter


# voteAge = int(input("Enter age: "))
# if voteAge >= 18:
#     print("You are Eligible")
    

# elif voteAge != 18:
#     print('You Are too Young')
#     voteAge = int(input("Enter age: "))
#     Counter =+ 1 

# else:
#     voteAge = int(input("Enter age: "))



voteAge = int(input("Enter age:"))

try:
    if voteAge >= 18:
        print("you are eligible")

    elif voteAge != 18:
        print("You way too young")
        voteAge = int(input("Enter age: "))

    else:
         voteAge = int(input("Enter age: "))

except ValueError:
    print('an error occured')