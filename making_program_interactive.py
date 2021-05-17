myName=input("please enter your name : ")
myAge=input("Please enter your age : ")

print("my name is ",myName," and I am ",myAge," years old.")
print("my name is %s and I am %s years old." %(myName,myAge))
print("my name is {0} and I am {1} years old.".format(myName,myAge))

##########triple quotes############
#when we print something under triple quotes they get printed in the same format as they are
print("""
Hello this is 
example of 
triple quotes
""")

########escape character###########
print("Hello\tworld") #tab space
print("Hello\nworld") #new line
print("Hello\\world") #adding a slice
print("Hello\"world") #adding a quotes
