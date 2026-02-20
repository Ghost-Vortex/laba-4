class EuropeanSocket:
    def voltage(self):
        return 230

class USASocket:
    def voltage(self):
        return 120

class Adapter(EuropeanSocket):
    def voltage(self):
        return 120
if __name__ == "__main__":
    euro = EuropeanSocket()
    usa = Adapter()
    print(euro.voltage())
    print(usa.voltage())
