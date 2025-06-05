tpl_numbers=(1,2,3,4,2,2,2,2)
tpl_city='Surat','Baroda'
print(tpl_numbers)
print(type(tpl_numbers))
for i in tpl_numbers:
    print(i)
print(tpl_numbers.count(2),tpl_numbers.index(4))
print(tpl_numbers[2:5])
lst_new=list(tpl_numbers)
print(lst_new)
for i in range(0,len(lst_new)):
    lst_new[i]+=10

new_tple=tuple(lst_new)
print(new_tple)
print(tpl_numbers[2:5])

