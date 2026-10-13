# implementation of single threading - flow of execution line by line
import time
class demo:
    def printname(self):
        op =['nibba','nibbi']
        for i in op:
            print(i)
            time.sleep(2) # after 2 secs nibbi will executed
    def printnum(self):
        for i in range(4):
            print(i)
            time.sleep(2)# each values takes 2 secs execute
    def add(self):
        a = 10
        b = 20
        c = a + b
        print(c) # no time delay here
result = demo()
result.printname()
result.printnum()
result.add()

# multi thraeding - multiple line of code doing multiple task simultaneously
import time
from threading import Thread
class task1(Thread):
    def run(self):
        op =['nibba','nibbi','sundra','sundri']
        for i in op:
            print(i)
            time.sleep(4)
class task2(Thread):
    def run(self):
        for i in range(4):
            print(i)
            time.sleep(4)
class task3(Thread):
    def run(self):
        a = 10
        b = 20
        c = a + b
        print(c)
f1 = task1()
f2 = task2()
f3 = task3()
f1.start()
f2.start()
f3.start()