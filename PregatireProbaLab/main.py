# Benotung:

# 1.a 3.5 Punkte
# 1.b 1 Punkt
#
# 2.a 2.5 Punkte
# 2.b 2 Punkte
#
# Insgesamt: 9 Punkte

# 2.
# a. Es wird die Klasse BinaryNumber angegeben, die eine Zeichenfolge aus 0 und 1 enthält, die bei der
# Erstellung des Objekts an die Klasse gesendet wird. Auf der Grundlage dieser Zeichenkette wird im
# Konstruktor eine Liste erstellt, in die jede Ziffer der Zeichenkette eingetragen wird.
# Schreiben Sie eine Funktion mit dem Namen "decimal_representation", die die Binärzahl anhand der Liste in
# eine Dezimalzahl umwandelt.

# Beispiel:
#             binary_number1 = BinaryNumber("11101")
#             binary_number2 = BinaryNumber("101")
#             print(binary_number1.decimal_represenation())  #11101 = 29
#             print(binary_number2.decimal_represenation())   #101 = 5

#
# b. Erstellen Sie die Klasse RepoBinaryNumber number, die als Attribut eine Liste von BinaryNumber-Objekten hat.
# Schreiben Sie eine Funktion, die die Summe dieser Zahlen berechnet. Tipp: Verwenden Sie die oben definierte
# Funktion "decimal_representation".

# Beispiel:
#             repo_binary_number = RepoBinaryNumber()
#             repo_binary_number.add(binary_number1)
#             repo_binary_number.add(binary_number2)
#             print(repo_binary_number.sum())#34