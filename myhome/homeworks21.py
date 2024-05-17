data_structure = [[1, 2, 3], {'a': 4, 'b': 5},
                  (6, {'cube': 7, 'drum': 8}),
                  "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
# n = 0
# k = 0
# 
# 
# def dict_():
#     di = i
#     data_list = list(di.items())
#     data_11 = data_list[0]
#     data_1 = len(data_11[0]) + data_11[1]
#     data_12 = data_list[1]
#     data_2 = len(data_12[0]) + data_12[1]
#     return data_1 + data_2

# def tuple_():

# def sum_glob():
#     global dict_, i
#     a = []
#     for i in data_structure:
#         if isinstance(i, list):
#             data_ = sum(i)
#             a.append(data_)
#         elif isinstance(i, dict):
#             d_summa = dict_()
#             a.append(d_summa)
#         elif isinstance(i, tuple):
#             a.append(i[0])
#     di = i[1]
#     t_summa = dict_()
#     a.append(t_summa)


#     print(a)
# sum_glob()
# print(data_ + data_1 + data_2)
#     data_list = list(i.items())
#     data_1 = data_list[0]

# data_1 = sum(data_structure[n])
# list_data_2 = list(data_structure[1].items())

# def dict_():
#     data_list = list(j.items())
#     data_11 = data_list[0]
#     data_1 = len(data_11[0]) + data_11[1]
#     data_12 = data_list[1]
#     data_2 = len(data_12[0]) + data_12[1]
#     return data_1 + data_2

result = []


def summa(name):
    for i in name:
        n = 0
        if isinstance(name[n], list):
            summa(name[n])
        elif isinstance(name[n], str):
            a = len(name[n])
            result.append(a)
        elif isinstance(name[n], tuple):
            summa(name[n])
        elif isinstance(name[n], int):
            result.append(name[n])
        elif isinstance(name[n], dict):
            b = list(name[n].items())
            summa(name[n])
        elif isinstance(name[n], set):
            summa(name[n])
        n += 1


summa(data_structure)
res = sum(result)
print(result)
print(res)
