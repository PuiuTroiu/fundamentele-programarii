class BinaryNumber():
    def __init__(self,lista_01):
        self.lista_01 = lista_01

    def decimal_reprezentation(self):
        cnt = 0
        dec_number = 0
        reverst_list_01 = reversed(self.lista_01)
        for bit in reverst_list_01:
            dec_number += int(bit)*(2**cnt)
            cnt += 1
        return dec_number

class Repo_Binary_Number:
    def __init__(self,lista_nr_binare):
        self.lista_nr_binare = lista_nr_binare

    def suma(self):
        s = 0
        for nr in self.lista_nr_binare:
            s += nr.decimal_reprezentation()
        return s

    def add(self,numar):
        self.lista_nr_binare.append(numar)




def main():
    repo = Repo_Binary_Number([])
    bin_number = BinaryNumber('11101')
    bin_number2 = BinaryNumber('101')
    repo.add(bin_number)
    repo.add(bin_number2)
    # print(bin_number.decimal_reprezentation())
    # print(bin_number2.decimal_reprezentation())
    print(repo.suma())
main()