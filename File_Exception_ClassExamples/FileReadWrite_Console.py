file=open("DataFromUser.txt",'w')
data=input("Please enter data!!!")
no_of_data=file.write(data)
print(f"{no_of_data} Data Written Successfully...")