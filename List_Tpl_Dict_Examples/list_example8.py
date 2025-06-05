lst_city=['Baroda','Surat','Rajkot','Ahmedabad','Ahm','Sur']
print("Before Sorting ",lst_city)
lst_city.sort()
print("After Sorting ",lst_city)
lst_city.sort(key=len,reverse=True)
print("After Sorting length",lst_city)
