# 2.
# a. Es wird die Klasse BinaryNumber angegeben, die eine Zeichenfolge aus 0 und 1 enthält, die bei der
# Erstellung des Objekts an die Klasse gesendet wird. Auf der Grundlage dieser Zeichenkette wird im
# Konstruktor eine Liste erstellt, in die jede Ziffer der Zeichenkette eingetragen wird.
# Schreiben Sie eine Funktion "sum", die zwei BinaryNumber-Objekte auf der Grundlage ihrer Liste
# addiert. Die beiden Zahlen können unterschiedliche Längen haben.

# Fügen Sie der Funktion einen Parameter "return_list" hinzu, der bestimmt, was die Funktion zurückgibt.
#       1. Wenn "return_list" True ist, gibt die Funktion die Binärzahl als Liste zurück.
#       2. Wenn "return_list" False ist, gibt die Funktion die Binärzahl als String zurück.

# Beispiel:
#       binary_number1 = BinaryNumber("101")
#       binary_number2 = BinaryNumber("1110")
#       res_sum = binary_number1.sum(binary_number2, return_list=False)
#       res_sum = binary_number1.sum(binary_number2, return_list=True)

# b.
# Erstellen Sie die Klasse RepoBinaryNumber number, die als Attribut eine Liste von BinaryNumber-Objekten hat.
# Schreibe eine Funktion "sum_all", die die Summe der ungeraden Zahlen zurückgibt. Bemerkungen:
#   1. Verwenden Sie die in Punkt a) definierte Funktion
#   2. Nur die mit der Binärzahl verbundene Liste kann zur Bestimmung der Parität verwendet werden.

# Beispiel:
#       repo_binary_number = RepoBinaryNumber()
#       repo_binary_number.add(binary_number1)
#       repo_binary_number.add(binary_number2)
#       print(repo_binary_number.sum_all())

class Binary_Number():
    def __init__(self,str_01):
        self.str_01 = str_01
        self.lista_01 = []

    def creare_lista(self,str):
        lista = []
        for nr in str:
            lista.append(int(nr))
        return lista


    def res_sum(self,numar2,return_list:bool):
        reversed_nr1_str = self.str_01[::-1]
        reversed_nr2_str = numar2.str_01[::-1]
        print(len(reversed_nr1_str))
        print(reversed_nr2_str)
        if len(reversed_nr1_str) > len(reversed_nr2_str):
            dif = len(reversed_nr1_str) - len(reversed_nr2_str)
            for ind in range(dif):
                reversed_nr2_str += '0'
        elif len(reversed_nr1_str) < len(reversed_nr2_str):
            dif = len(reversed_nr2_str) - len(reversed_nr1_str)
            for ind in range(dif):
                reversed_nr1_str += '0'
        # Fiecare cifra are acelasi numar de caractere0 sau 1--> s a adugat 0 la cel care are mai putine
        l1 = self.creare_lista(reversed_nr1_str)
        l2 = self.creare_lista(reversed_nr2_str)

        l3 = []
        carry = 0
        for ind in range(len(reversed_nr1_str)):
            cifra = (int(reversed_nr1_str[ind]) + int(reversed_nr2_str[ind]))
            if carry == 0:
                if cifra == 0 or cifra == 1:
                    if cifra == 0:l3.append('0')
                    else: l3.append('1')
                else:
                    l3.append('0')
                    carry = 1
            else:
                if cifra == 0 and carry == 1:
                    l3.append('1')
                    carry = 0

                elif cifra >= 1 and carry == 1:
                    l3.append('0')
                    carry = 1
        if carry == 1:
            l3.append('1')
        # print(l3)
        l4 = list(reversed(l3))
        if return_list is True:
            return l4
        else:
            nr = ''
            for i in range(len(l4)):
                nr += l4[i]
            return nr

class Repo_Binary_Number():
    def __init__(self,lista_numere):
        self.lista_numere = lista_numere

    def sum_all(self):
        s = ''
        nr = ''
        for str in self.lista_numere:
            if str.str_01[-1] == '1':#impar
                nr = str
            break

        for str2 in self.lista_numere[self.lista_numere.index(nr):]:
            print(f'{str2.str_01}')
            if str2.str_01[-1] == '1':
                # print(str2.str_01)
                s = nr.res_sum(str2, False)
                # print(f"s={s}")
        return s




def main():
    numar = Binary_Number("1010")
    numar2 = Binary_Number("1001")
    print(f"aici{numar.res_sum(numar2,False)}")
    repo = Repo_Binary_Number([Binary_Number('0101'),Binary_Number('101'),Binary_Number('1001')])
    print(repo.sum_all())
main()