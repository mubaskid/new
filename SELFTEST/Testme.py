try:

    ReadMe = open('Hello world', 'w')
    ReadMe.write('Hello how are you \n')
    ReadMe.write('Are feeling Okay')
    ReadMe.close()
    print(ReadMe)
except IOError:
    print('such file does not exist!!')

else:
    print('file sucessfully opened')