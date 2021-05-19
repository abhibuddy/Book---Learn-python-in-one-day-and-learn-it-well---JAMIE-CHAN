#conditional statements
print(5!=2)
print(5>2)
print(2<5)
print(2<=5)
print(2>=2)
print(2==2)
userInput=input("please enter 1 or 2 :")
if userInput=="1":
    print(" Hello How are you ? you just entered 1 ")
elif userInput=="2":
    print(" Python Rocks, You just entered 2 ")
else :
    print("print enter a valid number")

#inline if
num=10 if userInput == "1" else 20


print("value of num is : ",num)
print("this is choice A" if userInput=="1" else "this is another task")
###for loop###
pets=["cat","dog","cow","rabbit"]
for animal in pets:
    print(animal)
for index, animal in enumerate(pets):
    print(index," --> ", animal)

##lopping through Dictionary##
age={"peter":30,"john":7}
for i in age :
    print(i,"-->",age[i])
#same things we can achieve using .items()
for i,j in age.items():
    print(i,"-->",j)

#range function
for i in range(4,10,2):
    print(i)

#while loop
counter = 5
while counter > 0 :
    print("counter =",counter)
    counter-=1
print("")
# Break and Continue statements
j=0
for i in range(5):
    j=j+2
    print("i= ",i,"j =",j)
    if j==6:
        # break
        continue

#try-catch statement
try:
    userInput1=int(input("please enter a number : "))
    userInput2=int(input("please enter another number : "))
    answer = userInput2/userInput1
    print("the answer is : ",answer)
    myfile=open("missing.txt","r")
except ValueError: # if we don't enter a number
    print("Error : you didn't enter a number")
except ZeroDivisionError : #if this error occurs it will stop further execution
    print("Error : Cannot divide by zero")
except Exception as e : #for all other exception
    print("unknown Error : ", e)

#other errors are : IOError ImportError IndexError KeyError NameError TypeError