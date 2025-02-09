# Benotung:

# 1.a 3.5 Punkte
# 1.b 1 Punkt
#
# 2.a 3.5 Punkte
# 2.b 1 Punkt
#
# Insgesamt: 9 Punkte

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

# 2.
# a. Erstellen Sie eine Klasse namens "CalendarDate", die drei werte als Klassenvariable hat.
#
# Schreiben Sie eine Funktion "is_day_possible" die uberprüft ob diese Klasse ein richtige Datum enthält

#    Beispiel: für 19/01/2024 is_day_possible - TRUE
#              für 30/02/2023 is_day_possible - FALSE

# b.
# Erstellen Sie eine Klasse "FreeDatesYear", die eine Liste von Datum (CalendarDate-Objekten) enthält.
# Definieren Sie eine Funktion "add_date" in dieser Klasse, die eine neue CalendarDate zur Liste hinzufügt.
#
#   Beispiel:
#       my_free_days_this_year = FreeDatesYear()
#       my_free_days_this_year.add_date(my_day1)
#       my_free_days_this_year.add_date(my_day2)
# Überfrüfen Sie das Datum gültig ist. Benutzen Sie "is_day_possible".
