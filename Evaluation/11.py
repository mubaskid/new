def checkpalindrome(number):

    number = str(number)
    if number[0]==number[-1] and number[1]==number[-2]:
        return True

    else:
        return False


print(checkpalindrome(465))
print(checkpalindrome(645))
print(checkpalindrome(12345))