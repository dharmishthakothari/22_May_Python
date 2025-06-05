import random
number=random.randint(10,20)
status=True
while status:
    i=int(input("Guess the number::"))
    if i==number:
        break
    elif i<number:
        print(f"{i} is lesser then number")
    elif i>number:
        print(f"{i} is greater then number")
    

#print(number)