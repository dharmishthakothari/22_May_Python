file =open("MyGreeting.txt","w")
#data="Good Morning !!!"
data=['This is my First String\n','This is my Next String\n','Four','Five','Six']
file.writelines(data)
#file.write(data)
file.close()

fileRead=open("MyGreeting.txt","r")
print(fileRead.read())
fileRead.close()