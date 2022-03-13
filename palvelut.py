import random



class Asiakas():
    """Luokka, joka kuvaa Asiakkaan.
    :ivar nimi: Asiakkaan nimi
    :type nimi: str
    :ivar ika: Asiakkaan ikä
    :type ika: int
    """
    
    def __init__(self, nimi, ika):
        """Konstruktori
        """
        self.nimi= nimi
        self.ika = ika

    def get_nimi(self):
        return self.nimi
        """funktio joka palauttaa nimen
        type nimi: str
        """

    def set_nimi(self, uusinimi):
        try:
            if uusinimi != "":
                self.nimi= uusinimi
        except ValueError:
            raise ValueError("Kannattaa antaa uusi nimi")
        """funktio joka asettaa nimen arvon tilalle uuden nimen
        type uusinimi: str
        """
        

    def get_ika(self):
        return self.ika
        """funktio joka palauttaa Asiakkaan iän
        type ika: str"""

    def set_ika(self, uusi_ika):
        try:
            if uusi_ika != "":
                self.ika = uusi_ika
        except ValueError:
            raise ValueError("Kannattaa antaa uusi ikä")
        """Setteri funktio joka asettaa iän arvon tilalle uuden iän
        type uusi_ika: str"""
        
            
    
    def _luo_nro(self):

        nro1 = random.randint(0, 9)
        nro2 = random.randint(0, 9)
        nro3 = random.randint(0, 9)
        nro4 = random.randint(0, 9)
        nro5 = random.randint(0, 9)
        nro6 = random.randint(0, 9)
        nro7 = random.randint(0, 9)
        nro8 = random.randint(0, 9)

        asiakasnro = f'{nro1}{nro2}-{nro3}{nro4}{nro5}-{nro6}{nro7}{nro8}'
        return asiakasnro
        """Funktio joka palauttaa 8 eri numeroa satunnaisesti 0 ja 9 väliltä
        type nro1-nro8: int""" 

    def get_asiakasnro(self):
        return asiakasnro
        """funktio joka palauttaa asiakasnumeron
        type asiakasnro: str f"""



class Palvelu():
    def __init__(self, tuotenimi, asiakkaat=[]):
        """Konstruktori
        """
        self.tuotenimi=tuotenimi
        self.asiakkaat=[]

    def __luo_asiakasrivi(self, Asiakas):
         print(f'{Asiakas.get_nimi()},{Asiakas.get_asiakasnro()}, on {Asiakas.get_ika()}-vuotias')
         """Luo asiakasrivin käyttämällä get metodeja
        Asiakas type: class
        """

    def lisaa_asiakas(self, Asiakas):
        asiakas = input("Anna Asiakas: ")
        try:
            if asiakas == True:
                self.asiakkaat.append(asiakas)
        except ValueError:
            raise ValueError ("Kannattaa antaa uusi asiakas")
        """Lisää annetun asiakkaan asiakkaat listaan ja nostaa ValueErrorin jos ei anneta asiakasta
        type asiakas:: str
        """
            

    def poista_asiakas(self, Asiakas):
        asiakas = input("Anna Asiakas: ")
        try:
            if asiakas == True:
                self.asiakkaat.remove(asiakas)
        except ValueError:
            raise ValueError ("Kannattaa antaa uusi asiakas")
        """Poistaan annetun asiakkaan asiakaat listasta ja nostaa ValueErrorin jos ei anneta asiakasta
        type asiakas: str
        """

    def tulosta_asiakkaat(self):
        print(self.__luo_asiakasrivi())
        """Tulostaa luodun asiakasrivin käyttämällä luo_asiakasrivi metodia
        """


class ParempiPalvelu(Palvelu):
    def __init__(self, tuotenimi, edut=[]):
        """Konstruktori
        """
        super().__init__(tuotenimi)
        self.edut=[]

    def lisaa_etu(self, etu):
        etu = input("Anna Etu: ")
        try:
            if etu == True:
                self.edut.append(self, etu)
        except ValueError:
            raise ValueError ("Anna uusi etu")
        """Lisää edun edut listaan ja jos ei anneta arvoa nostaa ValueErrorin
        type etu: str
        """

    def poista_etu(self, etu):
        etu = input("Anna Etu: ")
        try:
            if etu == True:
                self.edut.remove(asiakas)
        except ValueError:
            raise ValueError ("Anna uusi etu")
        """Poistaa edun edut listasta ja jos ei anneta arvoa nostaa ValueErrorin
        type etu: str
        """

    def tulosta_edut():
        print(edut)
        """Tulostaa edut listan
        type edut: list
        """
