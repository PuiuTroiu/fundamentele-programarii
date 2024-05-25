from Entities.address import Address
class Student:
    def __init__(self,nume:str,adresa:Address):
        self.nume = nume
        self.adresa = adresa

    def __str__(self):
        return f'Nume: {self.nume}, Adresa:{self.adresa}'

    def __eq__(self, other):
        return self.nume == other.nume #and self.address == other.address -> terbuie implementat eq in clasa adresa

    def __lt__(self, other):
        return self.nume < other.nume
