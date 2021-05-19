class ParentClass:
    def __init__(self):
        self.a=1
        print("parent class object created")
    def someMethod(self):
        print("Hello")
class ChildClass(ParentClass):
    def __init__(self):
        print("child class object created")

parent = ParentClass()
child = ChildClass()
#isinstance() method to check whether an object is instance if a class ?
print(isinstance(parent,ParentClass))
print(isinstance(child,ChildClass))
print(isinstance(5,int))
print(isinstance(child,ParentClass))
print(isinstance(parent,ChildClass))
print(isinstance(parent,(ParentClass,int)))
try:
    isinstance(parent,MyClass)
except NameError:
    print("No such Class")
#issubclass() method to find whether a class is subclass of other ?
print(issubclass(ParentClass,ChildClass))
print(issubclass(ChildClass,ParentClass))
print(issubclass(ParentClass,(ParentClass,int)))

#hasattr() to check an object has attr ?
print(hasattr(parent,'a'))
print(hasattr(parent,'somemethod'))
print(hasattr(parent,'b'))

