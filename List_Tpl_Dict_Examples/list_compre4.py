lst_numbers =[23,34,22,56,77,81]
# lst_even_list=[]
# for i in lst_numbers:
#     if i%2==0:
#         lst_even_list.append(i)
# print(lst_even_list)
lst_even_list=[i for i in lst_numbers if i%2==0]
print(lst_even_list)