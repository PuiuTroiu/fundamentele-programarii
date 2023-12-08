# 2

def verificare_diag(matrix):
    rez=[]
    for i in range(len(matrix)):
        sum_linie = 0
        for j in range(len(matrix[i])):
            if i != j:
                sum_linie += matrix[i][j]

            # if sum_linie == matrix[i][i]:
            #     rez.append(True)
            # else:
            #     rez.append(False)
            rez.append(sum_linie == matrix[i][i])
        return rez

def test_sum_diag():
    assert verificare_diag(
       [[4,3,1],
       [1,2,1],
       [0,5,1]]) == [True,False,True]

    assert verificare_diag(
        [[1,2,3],
         [1,2,1],
         [0,4,0]]
    )== [False,True,False]


###################################################################

# 4

def max_line_file():
    f = open(filename,'r')
    rez =[]
    for line in f:
        max_len = 0
        max_word =''
        words = line.split(' ')
        word = word.strip()
        for word in words:
            if len(word) > max_len:
                max_word = word
                max_len = len(word)
        rez.append(max_len)
    f.close()
    return rez



def test_max_line_file():
    assert max_line_file('data.input') == [4,4]


#####################################################################################################

# 5

def is_palindrom(word):
    return word == word[::-1]

def find_count(filename,word):
    f = open(filename,'r')
    count = 0

    for linie in f:
        words = linie.split(' ')

        for w in words:
            if word == w.strip():
                count += 1
    f.close()
    return count

def count_pali(filename):
    f = open(filename,'r')
    rezult = {}

    for line in f:
        words = line.split(' ')

        for word in words:
            if is_palindrom(word):
                rezult[word] = find_count(filename,word.strip())

    f.close()
    return rezult
def test_count_pali():
    assert count_pali('data2.input') == {'anna':2,'abbcbba':1,'abba':2}

######################################################################################

# 1

def suma_div(nr):
    suma = 1
    for i in range (2,nr//2+1):
        if nr % i == 0:
            suma+=i
    return nr == suma


def suma_coloane(matrix):
    flag = True
    for i in range(len(matrix)):
        sum = 0
        for j in range(len(matrix[i])):
            sum += matrix[j][i]
        if suma_div(sum) == False:
            return False
    return True

def test_numar_perfect():
    assert suma_coloane([[4,3,10],[1,2,10,],[1,1,8]]) == True
    assert suma_coloane([[4,3,10],[1,2,10,],[1,3,8]]) == False


##################################################################################

# 3

def verificare_matrice_serpuita(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i % 2 ==0:
                if i == 0:
                    if matrix[i][j+1]-matrix[i][j] != 1:
                        

def test_matrice_serpuita():
    assert verificare_

def main():
    test_numar_perfect()

main()
