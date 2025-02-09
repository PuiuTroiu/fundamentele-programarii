# Erstellen Sie eine Klasse "FreeDatesYear", die eine Liste von Datum (CalendarDate-Objekten) enthält.
# Definieren Sie eine Funktion "add_date" in dieser Klasse, die eine neue CalendarDate zur Liste hinzufügt.
#
#   Beispiel:
#       my_free_days_this_year = FreeDatesYear()
#       my_free_days_this_year.add_date(my_day1)
#       my_free_days_this_year.add_date(my_day2)
# Überfrüfen Sie das Datum gültig ist. Benutzen Sie "is_day_possible".
import datetime
class CalendarDate:
    def __init__(self,zi,luna,an):
        self.zi = zi
        self.luna = luna
        self.an = an

    def is_day_possible(self):
        try:
            datetime.date(self.an, self.luna, self.zi)
            return True
        except ValueError:
            return False

    def __str__(self):
        return f"{self.zi}.{self.luna}.{self.an} "


class FreeDatesYear:
    def __init__(self,lista_date):
        self.lista_date = lista_date

    def adaugare_data_lista(self,data):
        if data.is_day_possible() is True:
            self.lista_date.append(data)
        else:
            print(f"Ziua {data.zi}, luna {data.luna} si anul {data.an} nu sunt valide")

    def afisare_lista(self):
        for dati in self.lista_date:
            print(dati)

def main():
    my_free_dates = FreeDatesYear([])
    data1 = CalendarDate(12,2,2024)
    data2 = CalendarDate(39,2,2024)
    data3 = CalendarDate(12,12,2024)

    my_free_dates.adaugare_data_lista(data1)
    my_free_dates.adaugare_data_lista(data2)
    my_free_dates.adaugare_data_lista(data3)
    my_free_dates.afisare_lista()

main()

# 1.
# a. Geben sei eine Textdatei mit dem Namen "zahlen.txt" an, die in jeder Zeile
# zwei Werte enthält, eine Zahl und einen Index, getrennet durch eine Komma ",",
# schreiben sie eine Funktion "my_sum", die:
#     - einen Parameter names "is_odd" enthält
#     - einen Parameter für den Name der Datei enthält
#     - aus der angegebenen txt-Datei "zahlen.txt" liest
#     - die Summe der Primzahlen berechnet.
#
# Die Berechnung der Summe erfolgt nach folgenden Regeln:
#     1. Falls "is_odd" True ist, berechnet man die Summe der Primzahlen (von der ersten Spalte) wo Index
#     (die zweite Spalte aus der Datei) ungerade (odd) ist
#     2. Falls "is_odd" False ist, berechnet man die Summe der Primzahlen (von der ersten Spalte) aus der
#     ganzen Datei
from functools import reduce
from math import sqrt


# Es wird erwartet, dass die Lösung map, filter oder reduce und andere mathematische
# Operationen, falls erforderlich, benützt.

# b. Schreiben Sie 2 Testfälle für die Funktion (einen für 'is_odd=True' und einen für 'is_odd=False')

def nr_prim(y):
    x = int(y[0])
    nr_2 = int(y[1])
    if x < 2: return False
    elif x != 2 and x % 2 == 0:return False
    else:
        for nr in range(3,int(sqrt(x))):
            if x % nr == 0:
                return False
    return True
    # return False
def my_sum(is_odd,filename):
    f = open(filename,'r')
    content = f.readlines()
    numere = list(map(lambda x:x.strip().split(','),content))
    # print(numere)

    numere_prime = list(filter(nr_prim,numere))
    print(numere_prime)

    if is_odd is True:
        l = list(filter(lambda x:int(x[1]) % 2 == 1,numere_prime))
        print(l)
        return reduce(lambda a,b:int(a[0])+int(b[0]),l)
    else:
        l = list(filter(lambda x:int(x[1]) % 2 == 0,numere_prime))
        return reduce(lambda a,b:int(a[0])+int(b[0]),l)