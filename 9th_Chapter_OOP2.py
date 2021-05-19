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

class ManagementStaff(Staff):
    def __init__(self,pName,pPay,pAllowance,pBonus):
        super().__init__('Manager',pName,pPay)
        self.allowance=pAllowance
        self.bonus=pBonus
    def calculatePay(self):
        basicPay=super().calculatePay()
        self.pay=basicPay+self.allowance
        return self.pay
    def calculatePerBonus(self):
        prompt='enter performance grade for %s :'%(self.name)
        grade = input(prompt)
        if (grade=='A'):
            self.bonus=1000
        else :
            self.bonus=0
        return self.bonus

class BasicStaff(Staff):
    def __init__(self,pName,pPay):
        super().__init__('Basic',pName,pPay)

peter=BasicStaff('peter',0)
john=ManagementStaff('john',0,1000,0)
print(peter.calculatePay())
print(john.calculatePay())
print(john.calculatePerBonus())