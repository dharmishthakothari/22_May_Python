lst_city=['ahemedabad','Baroda','Surat','']
lst_new_city=[]
print(lst_city)
for i in lst_city:
    print(i)
    if i!='':
        if i[0] in "aeiouu":
             lst_new_city.append(i)

print("New List ",lst_new_city)