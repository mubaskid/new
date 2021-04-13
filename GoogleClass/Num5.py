def ShowStars(n):
    for i in range(0, n):
        for i in range(0, i+1):
            print("* ",end="")
        print("\r")
n = 5
ShowStars(n)