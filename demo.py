
 

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


