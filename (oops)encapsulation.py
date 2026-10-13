# oops in python also includes class and object
# encapsulation - protecting the data by adding the extra layer to it
class Book:
    def __init__(self,value):
        self.pages = value
b1 = Book(100)
print(b1.pages)
b1.pages = 200
print(b1.pages)

class Book:
    def __init__(self):
        self.__pages = " " # protects the data
    def setData(self, value):
        self.__pages = value
    def getData(self):
        print(self.__pages)
output = Book()
# print(output.__pages) # error - not accessable
output.setData(100)
output.getData() # 100

class person:
    def __init__(self):
        self.__name = " "
    def setData(self, value):
        self.__name =  value
    def getData(self):
        return self.__name
output = person()
# print(output.__name)
output.setData("pradeep")
returnedValue1 = output.getData()
print(returnedValue1)
output.setData("rao")
returnedValue2 = output.getData()
print(returnedValue2)

# same program using multiple var and multiple return
class Person:
    def __init__(self):
        self. __name = ""
        self. __age =0
        self. __id = 0
        self. __gender = ""
        self. __place = ""
    def setData(self, name, age, id, gender, place):
        self. __name = name
        self. __age = age
        self. __id = id
        self. __gender = gender
        self. __place = place
    def getData(self):
        return self.__name,self.__age,self.__id,self.__gender,self.__place
output = Person()
output.setData("pradeep",25,1,"male","banglore")
r1,r2,r3,r4,r5 = output.getData()
print(r1)
print(r2)
print(r3)
print(r4)
print(r5)

# same concept using single method
# no need to use the setdata method if value is being assigned on the constructor itself
class Profile:
    def __init__(self,value):
        self.__name = value
    def getData(self):
        return self.__name
output = Profile("bindhu")
returnedValue = output.getData()
print(returnedValue)

# same concept using single method and user input
class Profile:
    def __init__(self,value):
        self.__name = value
    def getData(self):
        return self.__name
value = input("enter the name: ")
output = Profile(value)
returnedValue = output.getData()
print(returnedValue)

# property function in encapsulation - assigning multiple methods toa single common variable
class person:
    def __init__(self):
        self.__name = ""
    def getter(self):
        return self.__name
    def setter(self,value):
        self.__name = value
    getSet = property(getter,setter)
output = person()
output.getSet = "bindhu"
returnedValue = output.getSet
print(returnedValue) # bindhu(with property function)
output.setter("bindhu")
print(output.getter()) # bindhu(without property function)

# property decorator in encapsulation - accessing the value with common method
class person:
    def __init__(self):
        self.__name = ""
    @property # this works as a getter(gets the value)
    def dataAccess(self):
        return self.__name
    @dataAccess.setter # this works as setter(sets the value)
    def dataAccess(self, value):
        self.__name = value
output = person()
output.dataAccess = "bindhu"
print(output.dataAccess)