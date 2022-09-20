class Klienti:
    name=None
    numurs=None
    

    def __init__(self, name=None, numurs=None):
        self.name=name
        self.numurs=numurs
        
        self.get_data()

    def set_data(self, name=None, numurs=None):
        self.name=name
        self.numurs=numurs
        

    def get_data(self):
        print (self.name, 'numurs:', self.numurs)

class Pakalpojumi:
    pakalpojums=None
    cena=None
    ilgums=None

    def __init__(self, pakalpojums=None, cena=None, ilgums=None):
        self.pakalpojums=pakalpojums
        self.cena=cena
        self.ilgums=ilgums
        self.get_data()

    def set_data(self, pakalpojums=None, cena=None, ilgums=None):
        self.pakalpojums=pakalpojums
        self.cena=cena
        self.ilgums=ilgums
        

    def get_data(self):
        print (self.pakalpojums, 'cena:', self.cena, "ilgums:", self.ilgums)

klients1=Klienti("henriete", 743972492)
klients2=Klienti("anna", 287489427)

pakalpojumi1=Pakalpojumi("griešana", 32, 2)
