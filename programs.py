# reverse the value
def revstr(str):
    newstr = ""
    for i in str:
        newstr = i + newstr
    print(newstr)
ip = input("enter the value: ")
revstr(ip)

# remove the duplicate value
def removeDup(str):
    newstr = ""
    for i in str:
        if(i not in newstr):
            newstr = newstr + i
    print(newstr)
ip = input("enter the value:")
removeDup(ip)

# to total all the number
def sumoffall(num):
    total = 0
    while num > 0:
        rem = num % 10
        total += rem
        num = num // 10
    print(total)
ip = int(input("enter thr value: "))
sumoffall(ip)

#sum of all the digits
def sumOffall(num,total):
    if num <= 0:
        return total
    rem = num % 10
    total += rem
    num = num // 10
    return sumOffall(num, total)
ip = int(input("enter the number:"))
output = sumOffall(ip,0)
print(output)

# finding the largest  number
def largestnum(num):
    result = 0
    while num > 0: # 12>0 -true, 1 > 0- true , 0 > 0 - false
        rem = num % 10 # 12 % 10 - 2, 1 % 10 - 1
        if rem > result: # 2 >0 -true, 1>0 -true
            result = rem # result = 2
        num = num // 10 # 12 // 10 - 1, 1 // 10 - 0
    print(result) # 2
ip = int(input("enter the value: "))# 12
largestnum(ip)
        
# finding the second largest number
def largestnum(num):
    result = 0
    secondlar = 0
    while num > 0: 
        rem = num % 10    
        if rem > result:
            secondlar = result
            result = rem # 2
        elif rem > secondlar:
            secondlar = rem
        num = num // 10 
    return secondlar
ip =int(input("enter the value:"))# 12
output = largestnum(ip)
print(output) 

# prime number (the remainder value should never be 0)
def prime(num): # 5
    if(num<=1):
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
        return True # as none of the numbers are divisible by i == 0,finally it returns true which means prime number
ip = int(input("enter the number:"))
flag = prime(ip)
if flag:
    print("prime number")
else:
    print("not prime number")

# to print the prime and non prime numbers with user defined range
def prime(num):
    if(num <= 1):
        return False
    for i in range(2,num):
        if(num % i == 0):
            return False
        return True
firstNum = int(input("enter the first number:"))
lastNum = int(input("enter the last number:"))
print("prime numbers -")
for i in range(firstNum,lastNum+1):
    flag = prime(i)
    if flag:
        print(i)
print("non prime numbers -")
for i in range(firstNum,lastNum+1):
    flag = prime(i)
    if not flag:
        print(i)

# even or odd
def evenorodd(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
ip = int(input("enter the number: "))
evenorodd(ip)

# evenorodd
def evenorodd(num):
    return(num % 2 == 0)
firstNum = int(input("enter the first number:"))
lastNum = int(input("enter the last number:"))
print("even numbers -")
for i in range(firstNum,lastNum+1):
    flag = evenorodd(i)
    if flag:
        print(i)
print("odd numbers -")
for i in range(firstNum,lastNum+1):
    flag = evenorodd(i)
    if not flag:
        print(i)

def display(num):
    ip = [1,2,3,4]
    print(ip[num])
op = int(input("enter the number"))
display(op)

# leapyear or not
def leapyear(year):
    return (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0)
myinput = int(input("enter the year:"))
flag = leapyear(myinput)
if flag:
    print(myinput,"ia a leapyear")
else:
    print(myinput,"ia not a leapyear")

# leapyear and non leapyear
def leapyear(year):
    return (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0)
firstinput = int(input("enter the firstyear:"))
secondinput = int(input("enter the lastyear "))
print("leap years")
for i in range(firstinput,secondinput+4):
    flag =leapyear(i)
    if flag:
        print(i)
print("nonleap years")
for i in range(firstinput,secondinput+4):
    flag = leapyear(i)
    if not flag:
        print(i)

# count the numbers
num = int(input("enter the number"))
count = 0
if num < 0:
    num = num * -1# converts the negative number into positive number,for eg -101 will be 101
while num > 0:
    num = num //10
    count = count + 1
print(count)

# count the digits
def countvalues(num):
    if num < 0:
        num = num * -1
    count = 0
    while num > 0:
        num = num // 10
        count = count + 1
    return count
firstnum = int(input("enter the first number:"))
lastnum = int(input("enter the last number:"))
for i in range(firstnum,lastnum+1):
    output = countvalues(i)
    print(i,"consists of",output,"digit")

# amstrong number
def countnum(input):
    count =0
    while input > 0:
        input = input //10
        count +=1
    return count
def checkasn(num):
    temp = num
    asn = 0
    poweroff = countnum(num)
    if num < 0:
        num = num *-1
    while num > 0:
        base = num % 10
        asn = asn + (base ** poweroff)
        num = num //10
    if temp == asn:
        return True
    else:
        return False
myinput =int(input("enter the number:"))
output = checkasn(myinput)
if output:
    print(myinput,"is the amstrong number")
else:
    print(myinput,"is not amstrong number")

def countnum(input):
    count =0
    while input > 0:
        input = input //10
        count +=1
    return count
def checkasn(num):
    temp = num
    asn = 0
    poweroff = countnum(num)
    if num < 0:
        num = num *-1
    while num > 0:
        base = num % 10
        asn = asn + (base ** poweroff)
        num = num //10
    if temp == asn:
        return True
    else:
        return False
firstnum =int(input("enter the frist number:"))
lastnum = int(input("enter the last number"))
print("amstrong numbers")
for i in range(firstnum,lastnum):
    flag = checkasn(i)
    if flag:
        print(i)

# by using recursion amstrong number
def countnum(num,count):
    if num <= 0:
        return count
    num = num // 10
    count += 1
    return countnum(num,count)
def checkasn(num,asn,powerof,temp):
    if num <= 0:
        return asn == temp
    rem = num % 10
    asn = asn +(rem **powerof)
    num = num //10
    return checkasn(num,asn,powerof,temp)
ip = int(input("enter the number"))
powerof = countnum(ip,0)
output = checkasn(ip,0,powerof,ip)
if output:
    print(ip,"is amstrong")
else:
    print(ip,"not amstrong")

# to reverse a number(for eg,123)
num = int(input("enter the numbers:"))
temp = num
reversedNum =0
if num < 0:
    num = num * -1
while num > 0:
    rem = num % 10
    reversedNum = (reversedNum * 10) + rem
    num = num // 10
print(reversedNum)

# to reverse a number by using function(for eg,123)
def reverse(num):
    reversedNum =0
    if num < 0:
        num = num * -1
    while num > 0:
        rem = num % 10
        reversedNum = (reversedNum * 10) + rem
        num = num // 10
    return reversedNum
ip1 = int(input("enter the 1st number:"))
ip2 = int(input("enter the 2st number:"))
flag = reverse(ip1 + ip2)
print(flag)

def reverse(num):
    reversedNum =0
    while num > 0:
        rem = num % 10
        reversedNum = (reversedNum * 10) + rem
        num = num // 10
    return reversedNum
ip1 = int(input("enter the 1st number:"))
ip2 = int(input("enter the 2st number:"))
result1 = reverse(ip1)
result2 = reverse(ip2)
add = result1 + result2
print(add)
reversedSum = reverse(add)
print(reversedSum)

# give two numbers,add it and check if the reversed sum it is divisibility by 11 (reversedsum % 11 == 0 should be true)
def reverse(num):
    reversedNum =0
    while num > 0:
        rem = num % 10
        reversedNum = (reversedNum * 10) + rem
        num = num // 10
    return reversedNum
ip1 = int(input("enter the 1st number:"))
ip2 = int(input("enter the 2st number:"))
add = ip1 + ip2
print(add)
reversedsum = reverse(add) 
print(reversedsum % 11 == 0) 
if reversedsum :
    print("it is divisible by 11")
else:
    print("it is not divisible by 11")

 
#to reverse two numbers,add them,again reverse them and find if the reversed num is prime or not
def reverse(num):
    reversedNum =0
    if num < 0:
        num = num * -1
    while num > 0:
        rem = num % 10
        reversedNum = (reversedNum * 10) + rem
        num = num // 10
    return reversedNum
ip1 = int(input("enter the first number:"))
ip2 = int(input("enter the second number:"))
result1 = reverse(ip1)
result2 = reverse(ip2)
add = result1 + result2
print(add)
reversedsum = reverse(add)
print("reversed number total:",reversedsum)
def prime(num):
    if(num<=1):
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
        return True
output = prime(reversedsum)
if output:
    print(reversedsum,":prime number")
else:
    print(reversedsum,":not prime number")











   





