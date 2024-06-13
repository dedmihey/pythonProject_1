from itertools import combinations


def all_variants(n_list):
    n = 4
    for j in range(1, n):
        for i in combinations(n_list, j):
            yield i


al = all_variants('abc')
for i in al:
    print(''.join(i))
