class Temperature:
    def __init__(self, Farenheit, Celsius):
        self.Farenheit = Farenheit
        self.Celsius = Celsius
    def convertFarenheit(self, Celsius):
        return (Celsius*(9/5))+32

    def convertCelsius(self, Farenheit):
        return (Farenheit -32)*(9/5)
        

