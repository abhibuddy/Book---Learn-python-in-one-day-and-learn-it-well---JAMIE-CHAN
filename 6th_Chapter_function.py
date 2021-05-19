print("Hello World".replace("World","Universe"))

def checkIfPrime(numberToCheck):
    for x in range(2,numberToCheck):
        if numberToCheck%x==0:
            return False
        return True

print("the number is prime ? :",checkIfPrime(13))

#all default parameters should be placed at the end of parameters list
def defaultfun(a,b,c=5):
    print("a:",a," b : ", b," c : ",c)

defaultfun(10,20)

def addNumbers(*num):
    sum=0
    for i in num :
        sum = sum + i
    print("The Sum is : ",sum)
addNumbers(2,3,5)
addNumbers(2,3,5,10)

#to pass variable length key-value
def printMemberAge(**age):
    for i,j in age.items():
        print("Name : %s Age : %s"%(i,j))



printMemberAge(Peter=28,Ravi=50)

#to pass all at a time :
#def someFunction(farg,*arg,**kwarg)

import prime
answer = prime.checkIfPrime(13)
print("The answer from module imported is : ", answer)

#all the imports should be at the top of file
import random
print("The random number generated is : ",random.randrange(1,10))

###To use the module kept anywhere###
#import sys
#if 'c:\\MyPythonModules' not in sys.path:
#    sys.path.append('c:\\MyPythonModules')