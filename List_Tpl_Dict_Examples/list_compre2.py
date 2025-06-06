lst_numbers=[111,22,3,4]
lst_square=tuple(i*i for i in lst_numbers)
lst_qube=tuple(pow(i,3) for i in lst_numbers)
print(lst_square)
print(lst_qube)