# 1.
# a. Geben sei eine Textdatei mit dem Namen "tage.txt" an, die in jeder Zeile
# drei Werte enthält, Tag, Monat und Jahr, getrennet durch eine Schrägstrich "/",
# schreiben sie eine Funktion "my_day", die:
#     - einen Parameter names "is_day_duration" enthält
#     - einen Parameter für den Name der Datei enthält
#     - aus der angegebenen txt-Datei "tage.txt" liest
#     - die Difference zwischen die Tage berechnet und werte von Dauer in Tagen finden.
#
# Zum Beispiel: Für is_day_duration = 7 wir finden: 19/01/2024 - 12/01/2024 = 7 Tage

# Es wird erwartet, dass die Lösung map, filter oder reduce und andere mathematische
# Operationen, falls erforderlich, benützt.

# b. Schreiben Sie ein Testfall für die Funktion

def my_day(is_day_duration,filename):
    f = open(filename,'r')
    content = f.readlines()
    ore_zi_an = list(map(lambda x:x.strip().split('/'),content))
    f.close()
    ore_zi_an = list(filter(lambda x:int(x[0])>0 and int(x[0])<32,ore_zi_an))
    print(ore_zi_an)

def main():
    my_day(7,'tage.txt')

main()