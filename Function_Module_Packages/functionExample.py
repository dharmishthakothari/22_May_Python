def add(*num):
    sum=0
    for i in num:
        print(i)
        sum+=i
    print("in side function ",sum)
    return sum
def checkEven(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"


def emp_details(**kwars):
    print(kwars)
def person_details(age,name='-'):
    print(name,age)
def test_args(*args,name):
    print(name,args)

# answer=add(12)
# print("Sum = ",answer)
# print(checkEven(answer))
# answer=add(23,34)
# print("2 Sum = ",answer)
# answer=add(45.34,78.34)
# print("3 sum= ",answer)
emp_details(name='Qwerty',c_no=12345,salary=23456)
emp_details(name='lkjhg',salary=23456)
person_details('Dwij',20)
person_details('Yash')
person_details(34)
test_args('test',34,546,name='787')