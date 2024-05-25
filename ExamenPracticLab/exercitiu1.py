# 1.
# a. Geben sei eine Textdatei mit dem Namen "people.txt" an, die in jeder Zeile zwei Werte enthalt,
# eine Zeichenkette (der Name einer Person) und eine Zahl (das Alter der Person), getrennt durch
# eine Komma ",", schreiben Sie eine Funktion "count_palindromes", die:
#       -einen Parameter names "underage" enthält
#       -einen Parameter für den Namen der Datei enthält
#       -aus der angegebenen txt-Datei "people.txt" liest

# Die Funktion zählt die Personen in der Datei, deren Name ein Palindrom ist.
# Die Berechnung erfolgt nach folgenden Regeln:
#     1. Wenn "underage" True ist, zählt man die Personen, deren Name ein Palindrom ist,
#     die minderjährig sind
#     2. Wenn "underage" False ist, zählt man alle Personen, deren Name ein Palindrom ist

# Es wird erwartet, dass die Lösung map, filter oder reduce und andere mathematische
# Operationen, falls erforderlich, benützt.

# Beispiel für people.txt
#       -underage + palindrom:  2
#       -all names that are palindromes:  6

# b. Schreiben Sie 2 Testfälle für die Funktion (einen für 'underage=True' und einen für 'underage=False')

def count_palindromes(underage:bool,filename):
    f = open(filename,'r')
    content = f.readlines()
    oameni = list(map(lambda x: x.strip().split(','),content))
    f.close()
    oameni_palindorm = list(filter(lambda x: x[0].lower() == x[0][::-1].lower(), oameni))
    if underage is not True:
        return len(oameni_palindorm)
    else:
        minori = list(filter(lambda x: int(x[1])<18,oameni_palindorm))
        return len(minori)


def teste():
    assert count_palindromes(True,"people.txt") == 2
    assert count_palindromes(False,"people.txt") == 6
def main():
    teste()
    print(count_palindromes(False,"people.txt"))
    print(count_palindromes(True,"people.txt"))
main()