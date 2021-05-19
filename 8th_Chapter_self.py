class ProgStaff:
    companyName='programmingLab'  #class variable
    def __init__(self,pSalary):
        self.salary = pSalary #instance variable
    def printInfo(self):
        print("companyName is ",self.companyName)
        print("salary is ",self.salary)

peter = ProgStaff(2500)
john = ProgStaff(5000)

john.printInfo()
ProgStaff.companyName='programmingSchool'
peter.printInfo()
print("---------------------------------------")
print(john.companyName)
print(peter.companyName)

peter.salary=8000 # as only peter's salary increased
print("---------------------------------------")
print("John Salary : ",john.salary)
print("Peter Salary : ",peter.salary)

###two to call the printinfo() function###
print("first way to call the printinfo method")
john.printInfo()
print("second way to call the printinfo method")
ProgStaff.printInfo(john)




