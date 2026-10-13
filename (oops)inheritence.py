# inheritence - adding some more features with existing feature
# for eg - class a (parent class / super class) & class b (child class / sub calss)
# if class b(a) - nt is inside the child class 
# creating a object(class) for the child class
class A:
    def __init__(self):
        self.a= 10
class B(A):
    def __init__(self):
        A.__init__(self) # this specifies to move for class a
        self.b = 20
class C(B):
     def __init__(self):
         B.__init__(self) # this specifies to move for class b
         self.c = 30
output = C()
print(output.c)
print(output.b)
print(output.a)

class animal:
    def eat(self):
        print("animal is eating")
    def sleep(self):
        print("animal is sleeping")
    def breath(self):
        print("animal is breathing")
class tiger(animal):
    def eat(self):
        print("tiger is eating")
    def sleep(self):
        print("tiger is sleeping")
    def breath(self):
        print("tiger is breathing")
class deer(animal):
    def eat(self):
        print("deer is eating")
    pass # this skips the current method and goes for the same method name of parent class
    def breath(self):
        print("deer is breathing")
class monkey(deer):
    pass
outputt = tiger()
outputt.eat() # tiger is eating
outputt.sleep()# tiger is sleeping
outputt.breath()# tiger is breathing
outputd = deer()
outputd.eat() # deer is eating
outputd.sleep()# animal is sleeping
outputd.breath()# deer is breathing
outputm = monkey()
outputm.eat()# deer is eating
outputm.sleep()# animal is sleeping
outputm.breath()# deer is breathing

# types of inheritence
# single inheritence
# multi - level inheritence
# hierarchial inheritence
# multiple inheritence

# single inheritence - one parent one child
class A:
    def dispA(self):
        print("A")
class B(A):
    def dispB(self):
        print("B")
output = B()# last child class to be called
output.dispB() # B
output.dispA() # A

# multi- level inheritence - multiple parent multiple child
class A: # A is the parent
    def dispA(self):
        print("A")
class B(A): # b is the child and a is the parent
    def dispB(self):
        print("B")
class C(B): # c is the child and b is the parent
    def dispC(self):
        print("c")
output = C() # last child to be called
output.dispC()
output.dispB()
output.dispA()

# hierarchial inheritence - one parent multiple child
class A:
    def dispA(self):
        print("A")
class B(A):
    def dispB(self):
        print("B")
class C(A):
    def dispC(self):
        print("c")
outputB = B()
outputC = C()
outputB.dispB()
outputB.dispA()
outputC.dispC()
outputC.dispA()

# multiple inheritence - single child multiple parent
class A:
    def dispA(self):
        print("A")
class B:
    def dispB(self):
        print("B")
class C(A,B):
    def dispC(self):
        print("c")
output = C()
output.dispC()
output.dispB()
output.dispA()






    