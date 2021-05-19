class MethodDemo:
    a=1

    @classmethod
    def classM(cls): #instead of self here we have cls representing whole class
        print("class method cls.a : ", cls.a)

    @staticmethod
    def staticM():
        print("static method")
#calling class method
MethodDemo.classM()
#calling static method
MethodDemo.staticM()
#calling class method
mobj=MethodDemo()
mobj.classM()
#calling static method
mobj.staticM()