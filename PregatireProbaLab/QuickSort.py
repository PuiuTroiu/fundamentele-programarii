def rearanjare(st,dr,l):
    pivot = l[dr]
    index_curent = st
    for i in range(st,dr):
        if l[i] <= pivot:
            l[i],l[index_curent] = l[index_curent],l[i]
            index_curent += 1

    l[dr],l[index_curent] = l[index_curent],l[dr]
    return index_curent

def QuickSort(st,dr,l):
    if st <= dr:
        pindex = rearanjare(st,dr,l)
        QuickSort(st,pindex-1,l)
        QuickSort(pindex+1,dr,l)
def main():
    l = [4,2,5,3,6,7,1]
    QuickSort(0,len(l)-1,l)
    print(l)
main()