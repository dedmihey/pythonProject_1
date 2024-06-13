from itertools import combinations


def all_variants(n_list):
    n = 4
    for j in range(1, n):
        for i in combinations(n_list, j):
            print(''.join(i))


all_variants('abc')
