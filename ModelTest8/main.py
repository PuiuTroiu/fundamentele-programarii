import math


def read_list(filename):
    f = open(filename,'r')
    l = [int(num) for line in f for num in line.strip().split(',')]
    f.close()
    return l

def build(num):
    nr_cif = int(math.log10(num)+1)
    k = nr_cif//3
    nr_nou = 10
    ogl = 0
    p = 1
    while num != 0:
        uc = num % 10
        num //=1000
        nr_nou = nr_nou * 10 + uc
        ogl = ogl + p * uc
        p *=10
    return nr_nou



# def transfer(l,filename):
#     with open(filename,'w') as file:
#         for num in l:


# 239426492
# 294624932

def main():
    print(read_list('data.txt'))


main()