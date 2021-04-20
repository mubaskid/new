def checkpalindrome(number):

    number = str(number)
    if number[0]==number[-1] and number[1]==number[-2]:
        return True

    else:
        return False


print(checkpalindrome(12321))
print(checkpalindrome(55555))
print(checkpalindrome(12345))