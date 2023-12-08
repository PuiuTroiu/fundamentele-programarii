def inlocuire(cuvant_nou,cuvant_de_inlocuit):
    cnt_cuvant = 0
    f = open('cuvinte2.txt','r')
    linii = f.readlines()
    #f.close()

    g = open('cuvinte2.txt','w')
        
    for linie in linii:
        vec_cuvinte = linie.strip().split(' ')
        for i in range(len(vec_cuvinte)):
            if vec_cuvinte[i] == cuvant_de_inlocuit:
                cnt_cuvant += 1
                vec_cuvinte[i] = cuvant_nou
        linie_modificata = ' '.join(vec_cuvinte)
        # print(linie_modificata)
        g.write(linie_modificata)
        g.write('\n')


def cerinta():
    cuvant_nou = input("Introduceti noul cuvant: ")
    cuvant_de_inlocuit = input("Introduceti cuvantul ce vreti sa inocuiti: ")
    inlocuire(cuvant_nou,cuvant_de_inlocuit)
def main():
    cerinta()
main()