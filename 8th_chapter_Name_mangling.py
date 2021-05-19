class A:
    def __init__(self):
        self._x=5
        self.__y=6

varA=A()
print(varA._x)
# print(varA.__Y) will not work
print(varA._A__y) #use this instead of above code