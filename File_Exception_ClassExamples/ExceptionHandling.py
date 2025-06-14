try:
    data=int(input("Enter number "))
    print(data)
    ans=17/0
    print(ans)
    print("End of Try")
# except ZeroDivisionError:
#     print("In ZeroDivision")

except Exception:
    print("in exception")
except ValueError:
    print("in ValueError")
print("This is end of Program!!")