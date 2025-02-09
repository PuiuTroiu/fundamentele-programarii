
# c = []
# def merge_sort(l,st,dr):
#     if st == dr : return
#     else:
#         mij = (st+dr)//2
#         merge_sort(l,st,mij)
#         merge_sort(l,mij+1,dr)
#         inda = st
#         indb = mij+1
#         indc = 0
#         while inda <= mij and indb <= dr:
#             if l[inda] > l[indb]:
#                 c[indc] = l[indb]
#                 indc += 1
#                 indb += 1
#             else:
#                 c[indc] = l[inda]
#                 indc += 1
#                 inda += 1
#         while inda <= mij:
#             c[indc] = l[inda]
#             indc += 1
#             inda += 1
#         while indb <= dr:
#             c[indc] = l[indb]
#             indc += 1
#             indb += 1
#         for i in range(0,indc-1):
#             l[st+i-1] = c[i]
#

def selectionsort(l):
    for i in range(0,len(l)-1):
        for j in range(i+1,len(l)):
            if l[i] > l[j]:
                l[i],l[j] = l[j],l[i]
    return l

def insertionsort(l):
    for i in range(1,len(l)):
        j = i
        while j >= 1 and l[j-1] > l[j]:
            l[j-1],l[j] = l[j],l[j-1]
            j -= 1
    return l

def booblesort(l):
    for i in range(0,len(l)):
        for j in range(0,len(l)-1):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    return l
def mergeSort(array):
    if len(array) > 1:
            #  mij punctul in care se imparte array ul
            mij = len(array)//2
            L = array[:mij]
            M = array[mij:]

            # se merge in adancime si se imparte in cate 2
            mergeSort(L)
            mergeSort(M)

            i = j = k = 0

            #interclasare intre cele 2 jumatati

            while i < len(L) and j < len(M):
                if L[i] < M[j]:
                    array[k] = L[i]
                    i += 1
                else:
                    array[k] = M[j]
                    j += 1
                k += 1

            # Adaugare elemete lipsa
            while i < len(L):
                array[k] = L[i]
                i += 1
                k += 1

            while j < len(M):
                array[k] = M[j]
                j += 1
                k += 1
def main():
    array = [5,4,6,3,7,2,1]
    mergeSort(array)
    print(booblesort([7,1,4,3,5,2,6]))
    print(array)
main()

