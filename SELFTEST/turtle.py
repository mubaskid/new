import turtle
count = 0
try:
    while count < 20:
        for i in range(4):
            turtle.right(90)
            turtle.forward(90)


            turtle.left(90)
            turtle.forward(90)

            count += 3

            turtle.right(80)
            turtle.color("Blue")
            print(turtle.done)
            turtle()
except AttributeError:
    print('Error')