class Klienti:
    name=None
    surname=None
    pk=None
    numurs=None
    

    def __init__(self, name=None, surname=None, pk=None, numurs=None):
        self.name=name
        self.surname=surname
        self.pk=pk
        self.numurs=numurs
        
        
        self.get_data()

    def set_data(self, name=None, surname=None, pk=None, numurs=None):
        self.name=name
        self.surname=surname
        self.pk=pk
        self.numurs=numurs
        

    def get_data(self):
        print (self.name, self. surname)
        print('personas kods: ', self.pk)
        print('numurs:', self.numurs)

class Pakalpojumi:
    kategorija=None
    pakalpojums=None
    atlaide=None
    cena=None
    pieejams=None

    def __init__(self, kategorija=None, pakalpojums=None, atlaide=None, cena=None, pieejams=None):
        self.kategorija=kategorija 
        self.pakalpojums=pakalpojums
        self.atlaide=atlaide
        self.cena=cena
        self.pieejams=pieejams
        self.get_data()

    def set_data(self, kategorija=None, pakalpojums=None, atlaide=None, cena=None, pieejams=None):
        self.kategorija=kategorija 
        self.pakalpojums=pakalpojums
        self.atlaide=atlaide
        self.cena=cena
        self.pieejams=pieejams
        

    def get_data(self):
        print('pakalpojuma kategorija: ', self.kategorija)
        print('pakalpojuma nosaukums: ', self.pakalpojums)
        print('atlaide: ', self.atlaide)
        print('cena: ', self.cena)
        print('pieejams: ',self.pieejams)

klients1=Klienti("henriete", "ignatjeva", "3279327-282847", 743972492)
klients2=Klienti("linda", "kalnina", "27947-34274289", 287489427)
klients3=Klienti("anna", "zalite", "277-374289", 29489249427)
pakalpojumi1=Pakalpojumi("frizētava", "griešana", "20%", 20, True)
pakalpojumi2=Pakalpojumi("frizētava", "krāsošana", "10%", 40, True )
pakalpojumi3=Pakalpojumi("uzacu kopšana", "uzacu kopšana", "20%", 60, True)
