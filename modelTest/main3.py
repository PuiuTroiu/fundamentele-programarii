def read_matrix (file_name):
    f = open(file_name, 'r')

    matrix = []
    for line in f:
        l = []
        for el in line.strip().split(','):
            l.append(int(el))

        matrix.append(l)

    return matrix


def is_sparse(matrix):
    c0 = 0
    c1 = 0

    for line in matrix:
        for col in line:
            if col == 0:
                c0 += 1
            if col == 1:
                c1 += 1

    return c0 >= (c0+c1)*0.7


m = read_matrix('input.data')
print(is_sparse(m))
