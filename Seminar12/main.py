#suma numerelor dintr o lista
import math
def sumaListe(n,l):
    if n < 0:
        return 0
    return l[n] + sumaListe(n - 1,l)

#suma cifre pare

def sumacifrepare(nr):
    if nr == 0:
        return 0
    if nr % 10 % 2 == 0:
        return nr % 10 + sumacifrepare(nr//10)
    elif nr % 10 % 2 != 0:
        return sumacifrepare(nr//10)

#returnare ultima litera majuscula

def majuascula(n,l):
    if n < 0:
        return None
    else:
        if l[n] >= 'A' and l[n] <= 'Z':
            return l[n]
        else:
            return majuascula(n-1,l)


def nrvocale(n,l,voc):
    if n < 0:
        return 0
    if l[n] in voc:
        return 1 + nrvocale(n-1,l,voc)
    else:
        return nrvocale(n-1,l,voc)

def palindrom(n):
    if n < 10:
        return True
    nrcif = int(math.log(n,10))
    #a = n//10**(nrcif) % 10
    #b = n % 10
    if n % 10 != n//10**(nrcif) % 10:
        return False
    return palindrom(n % 10**(nrcif)//10)

##7

def sl(l):
    s = 0
    for el in l:
        if type(el) == list:
            s = s + sl(el)
        else:
            s = s + el
    return s


def elinlista(l,nr):
    if len(l) == 0:
        return False
    for el in l:
        if type(el) == list:
            return elinlista(el)
        else:
            if nr in l:
                return True
            else:
                return False


#4538

def CifDiferiteRec(n,k):
    if n < 10:
        if n == k:return 0
        else: return 1
    if n % 10 != k:
        return 1 + CifDiferiteRec(n//10,k)
    return CifDiferiteRec(n//10,k)

#4537

def CifEgaleRec(n,k):
    if n < 10:
        if n != k:
            return False
        return True
    if n % 10 == k:
        return CifEgaleRec(n//10,k)
    return False

def generareMatrice(n):
    matrice = []
    
def main():
    ##0
    #l = [1,2,3,4,5,6,7,8,9,10]
    #print(sumaListe(len(l)-1,l))

    ##1
    #nr = int(input("Number: "))
    #print(sumacifrepare(nr))

    ##2
    #l = "Mama merge la Piata cu Maria"
    #print(majuascula(len(l)-1,l))

    ##3
    #l = "Mama merge la Piata cu Maria"
    #print(nrvocale(len(l)-1,l,['a','e','i','o','u']))

    ##4
    #n = 12213
    #print(palindrom(n))

    ##7
    #print(sl([1, [1, [1, 2, 3], 1], 3]))

    #(CifDiferiteRec(4,4))

    print(CifEgaleRec(2222,2))


main()