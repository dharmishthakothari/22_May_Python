lst_city=['Ahemdabad','Bhopal','Mumbai','Delhi']
lst_state=['Gujarat','MP','Maharastra','Delhi','Goa']
lst_area=['Parimal','Bhopal Area','Boriwali']
lst_state_city=list(zip(lst_state,lst_city,lst_area))
tpl_state_city=tuple(zip(lst_state,lst_city,lst_area))
print(lst_state_city)
tpl=lst_state_city[2]
print("tpl ",tpl,tpl.index("Mumbai"))
print(lst_state_city[2][1])
print(tpl_state_city[2][1])