lst_number=[1,22,55,67,89,'Test']
for i in lst_number:
    if type(i)==int:
        if i%2==0:
            print(f"{i} is Even no")
        else:
            print(f"{i} is Odd no")
    else:
        print(f"{i} is not numeric")