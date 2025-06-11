def findFact(num):
    mul=1
    for i in range(1,num+1):
        mul*=i
    return mul
def checkPositive(num):
    if num>0:
        return True
    else:
        return False
