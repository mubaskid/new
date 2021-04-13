int(input('Please enter a speed: '))
def driversSpeed(speed):
    for speed in range(1, 70):
        if speed <= 70:
            print("Ok")
        elif speed == 80:
            print('Points: 2')

        else:
            if speed > 80:
                print('Points: 12 \n liscence suspended')
                
