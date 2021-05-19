class Staff:
    def __init__(self,pPosition,pName,pPay):
        self._position=pPosition
        self.name=pName
        self.pay=pPay
        print("creating staff object")
    def __str__(self):
        return " Position = %s\n Name = %s\n Pay = %s" %(self._position,self.name,self.pay)

    def calculatePay(self):
        hours=input("Enter number of hrs worked for %s : " %self.name)
        hourlyrate=input("enter the hourly rate for %s : " %self.name)
        self.pay=int(hours)*int(hourlyrate)
        return self.pay

    @property
    def position(self):
        print("Getter Method")
        return self._position

    @position.setter
    def position(self,value):
        if value=="Manager" or value == "Basic":
            self._position=value
        else:
            print("Position is invalid, No change made.")

officestaff1=Staff("Manager","Ravi",0) #intanciating an object
officestaff1.calculatePay()
print(officestaff1)
print("accessing the variable of the class")
print(officestaff1.position)
print(officestaff1.name)
print(officestaff1.pay)

officestaff1.position='CEO' #if we try to add anything other than "Basic" or "Manager"
