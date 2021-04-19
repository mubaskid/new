class Customer:
    def __init__(self, Name, Email, Address, Phone, StockOdered):
        self.Name = Name
        self.Email = Email
        self.Address = Address
        self.Phone = Phone
        self.StockOdered = StockOdered

    # def __str__(self, str):
    #     return f"""{self.Name}\t{self.Email}\t{self.Phone}\t{self.StockOdered}"""