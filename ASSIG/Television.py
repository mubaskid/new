class Television:
    def __init__(self, screen, switch, remote, size, type, brand, version, inches):
        self.screen = screen
        self.switch = switch
        self.remote = remote
        self.size = size
        self.type = type
        self.brand = brand
        self.version = version
        self.inches = inches

    def __init__(self, screen:str, switch:str, remote:str, size:str, type:str, brand:str, version:str, inches:float):
        self.screen = screen
        self.switch = switch
        self.remote = remote
        self.size = size
        self.type = type
        self.brand = brand
        self.version = version
        self.inches = inches

