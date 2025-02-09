
def sorted_merge(l1,l2):
    l3 = []
    i,j = 0,0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            l3.append(l1[i])
            i += 1
        elif l2[j] < l1[i]:
            l3.append(l2[j])
            j += 1
        else:
            l3.append(l1[i])
            i += 1
            j += 1

    return l3 + l1[i:] + l2[j:]

#101010-> 000111
def recursive_sort(l):
    if len(l) == 0:
        return []
    if l[0] == 0:
        return [0] + recursive_sort(l[1:])
    return recursive_sort(l[1:]) + [1]

def find_binary(l,start,End):
    if start > End:
        #return len(l)
        return End +1
    if l[start] != start:
        return start
    mid = (start + End)//2
    if mid == l[mid]:
        return find_binary(l,mid+1,End)
    else:
        return find_binary(l,start,mid)

def get_column(i,n,m):
    if len(m) != n * n:
        raise ValueError('Nu este patratica!!!')
    col = []
    for pos,ch in enumerate(m):
        if pos % n == i:
            col.append(ch)
    return col


def test_get_column():
    assert get_column(0,3,'012345678') == ['0','3','6']
    assert get_column(1,3,'012345678') == ['1','4','7']
    assert get_column(2,3,'012345678') == ['2','5','8']


def find1(l,n):
    if n == 0:
        if l[n] == 1:
            return 1
        else:
            return 0
    if l[n] == 1:
        return 1 + find1(l,n-1)
    else:
        return find1(l,n-1)


def letzenVorkommen(l,n,nr):
    if l[n] == nr:
        return n
    if n == 0:
        return -1
    return letzenVorkommen(l,n-1,nr)
def main():

    #print(sorted_merge([1,2,6,7],[2,4,6]))
    #print(recursive_sort([0,1,0,1,0]))
    #print(find_binary([0,1,2,4,5,6,7,8],0,len([0,1,2,4,5,6,7,8])-1))
    #test_get_column()
    # print(find1([1,2,3,1,2,9],len([1,2,3,1,2,9])-1))
    print(letzenVorkommen([1,2,3,6,2,8],5,1))
main()