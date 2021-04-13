class Stock:
    def __init__(self):
        self.Symbol = "company logo"
        self.Name = "LouisVuiton"
        self.PreviousClosingPrice = 123.0
        self.CurrentPrice = 100.0

    def GetSymbol(self):
        self.Symbol
        return 'company logo'

    def GetName(self):
        self.Name
        return 'LouisVuiton'

    def GetPreviousClosingPrice(self):
        self.PreviousClosingPrice = 123.0

    def SetPreviousClosingPrice(self):
        self.PreviousClosingPrice = 200.99

    def GetCurrentPrice(self):
        self.CurrentPrice = 100.0

    def SetCurrentPrice(self):
        self.CurrentPrice = 150.97


    def getChangePercentage(self):
        self.PreviousClosingPrice = 200.99
        self.CurrentPrice = 150.97
        self.ChangePercentage = 150.97
        return 150.97  