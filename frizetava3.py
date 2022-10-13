import itertools
import datetime
from datetime import time
from datetime import datetime
from re import X

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
        
class Klienti(Person):
    def __init__(self, name, surname, pk, numurs):
      print("Klienta dati")
      super().__init__(name, surname, pk, numurs)
      print("")

class Darbinieki(Person):
    def __init__(self, name, surname, amats, pk, numurs):
      print("Darbinieka dati")
      super().__init__(name, surname, pk, numurs)
      self.amats=amats
      print("amats", self.amats)
      print("")

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

class Izmantosana:
    pakalpojuma_sakuma_laiks=0
    pakalpojuma_beigu_laiks=0

    def __init__(self, pakalpojuma_sakuma_laiks=None, pakalpojuma_beigu_laiks=None):
        self.pakalpojuma_sakuma_laiks=pakalpojuma_sakuma_laiks
        self.pakalpojuma_beigu_laiks=pakalpojuma_beigu_laiks
        self.Izmantosana_info_print()

    def Izmantosana_info_print(self):
        print("Pakalpojuma sakuma laiks:"+ str(self.pakalpojuma_sakuma_laiks))
        print("Pakalpojuma beigu laiks:"+str(self.pakalpojuma_beigu_laiks))
        print("Pakalpojuma ilgums:"+str(self.pakalpojuma_beigu_laiks-self.pakalpojuma_sakuma_laiks))


        






darbinieks1=Darbinieki("amanda", "kocina ","friziere", "7247-52353", 37483472 )
darbinieks2=Darbinieki("zenta", "graudina ","friziere", "72457577-52353", 235352 )
darbinieks3=Darbinieki("evelina", "zala ","uzacu meistare", "7899-21414", 8067764 )
klients1=Klienti("henriete", "ignatjeva", "3279327-282847", 743972492)
klients2=Klienti("linda", "kalnina", "27947-34274289", 287489427)
klients3=Klienti("anna", "zalite", "277-374289", 29489249427)
pakalpojumi1=Pakalpojumi("frizētava", "griešana", "20%", 20, True)
pakalpojumi2=Pakalpojumi("frizētava", "krāsošana", "10%", 40, True )
pakalpojumi3=Pakalpojumi("uzacu kopšana", "uzacu kopšana", "20%", 60, True)
laiks1=Izmantosana(datetime(2022, 12, 16, 10), datetime(2022, 12, 16, 11))

now = datetime.now()

dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("laiks un datums=", dt_string)	
