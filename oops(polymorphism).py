# polymorphism - multiple behaviour for one object
class plane:
    def takeoff(self):
        print("plane is takeoff")
    def fly(self):
        print("plane is flying")
    def land(self):
        print("plane is landing")
class cargo(plane):
    #def takeoff(self):
        #print("cargo is takeoff")
    def fly(self):
        print("cargo is flying")
    def land(self):
        print("cargo is landing")
class passenger(plane):
    def takeoff(self):
        print("passenger is takeoff")
    def fly(self):
        print("passenger is flying")
    def land(self):
        print("passenger is landing")
class fighter(plane):
    def takeoff(self):
        print("fighter is takeoff")
    def fly(self):
        print("fighter is flying")
    def land(self):
        print("fighter is landing")
outputcargo = cargo()
outputpassenger = passenger()
outputfighter = fighter()
def outputOfAll(input):
    input.takeoff()
    input.fly()
    input.land()
outputOfAll(outputcargo)
outputOfAll(outputpassenger)
outputOfAll(outputfighter)

# polymorphism using super()
# if we use super() inside the method, it will fetches the value from the same of parent class method
class A:
    def __init__(self):
        self.a = 10
class B(A):
    def __init__(self):
        super().__init__() # when output.a is called it will goes to the A class to check the value (as B is not there here)
        self.b = 20
class C(A):
    def __init__(self):
        super().__init__() # when output.b is called it will goes to the A class to check the value (as B is not there here)
        self.c = 30
output = C()
print(output.c)
print(output.b)
print(output.a)

class A:
    def disp(self):
        print("A")
class B(A):
    def disp(self):
        super().disp()
        print("B")
class C(B):
    def disp(self):
        super().disp()
        print("C")
output = C()
output.disp()

class animal:
    def eat(self):
        print("animal is eating")
    def sleep(self):
        print("animal is sleeping")
class lion(animal):
    def eat(self):
        super().eat()
        #print("lion is eating")
    def sleep(self):
        super().sleep()
        print("lion is sleeping")
class tiger(animal):
    def eat(self):
        print("tiger is eating")
    def sleep(self):
        print("tiger is sleeping")
class monkey(animal):
    def eat(self):
        print("monkey is eating")
    def sleep(self):
        print("monkey is sleeping")
outputlion = lion()
outputtiger = tiger()
outputmonkey = monkey()
def outputofanimals(input):
    input.eat()
    input.sleep()
outputofanimals(outputlion)
outputofanimals(outputtiger)
outputofanimals(outputmonkey)

# difference between pass and super()
class animal:
    def eat(self):
        print("animal is eating")
    def sleep(self):
        print("animal is sleeping")
class lion(animal):
    def eat(self):
        super().eat()
    pass
output = lion()
output.sleep()
output.eat()

class animal:
    def eat(self):
        print("animal is eating")
    def sleep(self):
        print("animal is sleeping")
class human(animal):
    def eat(self):
        super().eat()
        super().sleep()
    def sleep(self):
        print("human is sleeping")
op = human()
op.eat()
op.sleep()

# method overriding
class A:
    def dispA(self):
        print("A")
class B(A):
    def dispB(self):
        print("B")
class C(B):
    def dispC(self):
        print("C")
class D(C):
    def displayAll(self):
        A.dispA(self)
        B.dispB(self)
        C.dispC(self)
output = D()
output.displayAll()

# mro rules
# if head is not found in tail, head should be removed
# if head is found in tail, then head should be removed






 
