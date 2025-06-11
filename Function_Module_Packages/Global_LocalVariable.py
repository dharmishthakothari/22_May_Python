def getDetials():
    global tech,age
    tech="Python"
    age=23
    print(name,age,tech)
name="Tops"
age=20
tech="DS"
print("Before function calling ",name,age,tech)
getDetials()
print("After function calling ",name,age,tech)
tech="DA"
print("After function calling ",name,age,tech)


