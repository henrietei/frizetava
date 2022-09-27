class Person:
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
        print(" ")

class Klienti(Person):
    def __init__(self, name, surname, pk, numurs):
        super().__init__(name, surname, pk, numurs)

    def klients(self):
        print("klienta dati")
        print(" ")

        """print (self.name, self. surname)
        
        print('personas kods: ', self.pk)
        print('numurs:', self.numurs)
        print (" ")"""
    
class Darbinieki(Person):
    darbs="darbinieka dati"
    def __init__(self, darbs, name, surname, amats, pk, numurs):
        
        super().__init__(name, surname, pk, numurs)
        self.darbs=darbs
        self.amats=amats
    def darbinieks(self):
        print("darbinieka dati")
        print(" ")

    
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
        print(" ")


darbinieks_arr=[Darbinieki("amanda", "kocina ","friziere", "7247-52353", 37483472 ), Darbinieki("zenta", "graudina ","friziere", "72457577-52353", 235352 ), Darbinieki("evelina", "zala ","uzacu meistare", "7899-21414", 8067764 )]
#darbinieks1=Darbinieki("amanda", "kocina ","friziere", "7247-52353", 37483472 )
#darbinieks1.darbinieks()
#darbinieks2=Darbinieki("zenta", "graudina ","friziere", "72457577-52353", 235352 )
#darbinieks3=Darbinieki("evelina", "zala ","uzacu meistare", "7899-21414", 8067764 )
klients1=Klienti("henriete", "ignatjeva", "3279327-282847", 743972492)
klients2=Klienti("linda", "kalnina", "27947-34274289", 287489427)
klients3=Klienti("anna", "zalite", "277-374289", 29489249427)
pakalpojumi1=Pakalpojumi("frizētava", "griešana", "20%", 20, True)
pakalpojumi2=Pakalpojumi("frizētava", "krāsošana", "10%", 40, True )
pakalpojumi3=Pakalpojumi("uzacu kopšana", "uzacu kopšana", "20%", 60, True)
