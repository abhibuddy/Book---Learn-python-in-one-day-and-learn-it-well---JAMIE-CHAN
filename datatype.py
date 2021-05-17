# int [integer]
userAge=20
mobileNumber=947004474

# float [float]
userHeight=1.82

# str [string]
userName="Peter"
userAge='30'
userFullName="peter"+"lee"
print(userName.upper())

# type casting in python
userAge=int('30')

message="%s is %d year old and he is %3.1f ft tall"%(userName,userAge,userHeight)
message_formatted="{0} is {1} year old and he is {2}ft tall".format(userName,userAge,userHeight)
print(message)
print(message_formatted)

# list
userAgelist=[21,22,23,24,25]
userAgelist[1]=50
print(userAgelist)
another_list=[1,2,3,"Hello"]
print(another_list)
print("last element from the list is ",another_list[-1])
another_list.append("How are you ? ") #adding an element in list
print("elements from 2nd index position to 3rd ",another_list[1:3])

# tuple
months=("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")
print("the last element in the tuple is : ", months[-1])
print("the first element in the tuple is : ", months[0])

# dictionary
myDict={"peter":38,"john":51,"Ravi":65}
print(myDict) #items in dict are not stored in same order
print(myDict.items())
print(myDict.keys())
print(myDict.values())
myDict["peter"]="it's new"
print(myDict.items()) #updating a value in dictionary