lst_fruits=['Apple','Mango','Cherry','Chicoo']
print(lst_fruits[1:5])
lst_fruits[1]='Banana'
print(lst_fruits)
lst_mango_type=['Mango',['Kesar','Hafus','Rajapuri','Desi']]

for i in lst_fruits:
    if isinstance(i,list):
        print(f"{lst_fruits} contains list {i}")
        break
else:
    print(f"{lst_fruits} doesn't contains list")
