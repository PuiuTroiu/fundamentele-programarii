def do_stuff(s1):
    arr = [0]*len(s1)

    for i in range (len(s1)):
        w = 2
        while w < s1[i] and s1[i]%w:
            w *= 2
        arr[i] = w

    for i in range(len(arr)):
        arr[i] = arr[i] <= s1[i]

    return arr

def test_do_stuff():
    assert do_stuff([12, 6, 9]) == [True, True, False]
    assert do_stuff([12, 6, 9]) == [True, True, True]


test_do_stuff()
print(do_stuff([12, 6, 9]))