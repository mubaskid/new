celsius = float(input('Enter temperature in celsius: '))

fahrenheit = 1.8 * celsius + 32
kelvin = 273.15 + celsius

print('%0.3f Celsius = %0.3f Fahrenheit.' % (celsius, fahrenheit))
print('%0.3f Celsius = %0.3f Kelvin.' % (celsius, kelvin))
