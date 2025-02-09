# Benotung:

# 1.a 3.5 Punkte
# 1.b 1 Punkt
#
# 2.a 3.5 Punkte
# 2.b 1 Punkt
#
# Insgesamt: 9 Punkte

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

# Es wird erwartet, dass die Lösung map, filter oder reduce und andere mathematische
# Operationen, falls erforderlich, benützt.

# b. Schreiben Sie 2 Testfälle für die Funktion (einen für 'is_odd=True' und einen für 'is_odd=False')

# 2.
# a. Erstellen Sie eine Klasse namens "BigNumber", die eine Zeichenkette als Klassenvariable hat.
# Diese Zeichenfolge enthält nur Ziffern, wobei die gesamte Zeichenfolge eine sehr große natürliche
# Zahl darstellt. Diese Zeichenkette wird an die Klasse übergeben, wenn die Klasse instanziiert wird.
# Die Klasse hat eine zweite Variable, eine Liste, in die alle Ziffern der Zeichenkette eingetragen
# werden. Dies kann im Konstruktor berechnet werden.
#
# Erstellen Sie eine Funktion in dieser Klasse, die die Summe von zwei BigNumbers auf der
# Grundlage der Liste berechnet. Die Funktion nimmt ein anderes BigNumber-Objekt als Parameter und
# gibt die Summe zurück (als String). Gehen Sie davon aus, dass die 2 Zahlen die gleiche Länge haben.

#    Beispiel:
#       my_number1 = BigNumber("56325663")
#       my_number2 = BigNumber("96325663")
#       my_sum = my_number1.add(my_number2)

# b.
# Erstellen Sie eine Klasse "NumberBox", die eine Liste großer Zahlen (BigNumber-Objekten) enthält.
# Definieren Sie eine Funktion "add_number" in dieser Klasse, die eine neue BigNumber zur Liste hinzufügt.
#
#   Beispiel:
#       my_number_box = NumberBox()
#       my_number_box.add_number(my_number1)
#       my_number_box.add_number(my_number2)
