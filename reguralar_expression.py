# regular expression are mostly used to validate user input in forms before saving it to the database
import re
# match()- checks if the given patter is at the beginning of the string
ip1 = "456 is my pin"
if re.match(r"\d{1}",ip1):
    print("it is found")
else:
    print("it is not found")

import re
ip1 = "my pin is 123"
if re.match(r"\d{1}",ip1):
    print("it is found")
else:
    print("it is not found")

# search - checks if there are given digits together
import re
ip1 = " my pin is 123"
if re.search(r"\d{3}",ip1):
    print("it is found")
else:
    print("it is not found")

#modifier - ignores the case
text = "PYTHON"
if re.search("python", text, re.IGNORECASE):
    print("found")

# findAll() - finds the given element and displays as per it
import re
ip2 = "hello 123, 456, 789"
ip2res = re.findall(r"\d{2}", ip2)
print(ip2res)

import re
ip2 = "helloo"
ip2res = re.findall(r"\D{2}", ip2)
print(ip2res)

import re
ip2 = "hello_123"
ip2res = re.findall(r"\w", ip2)
print(ip2res)

import re
ip2 = "hello world"
ip2res = re.findall(r"\s", ip2)
print(ip2res)

import re
ip2 = "hello world"
ip2res = re.findall(r"\S", ip2)
print(ip2res)

#sub() - replaces the matches
import re
ip3 = "my num is 856429875"
updatedip3= re.sub(r"\d", "*",  ip3)
print(updatedip3)

import re
ip3 = "my num is 856429875"
updatedip3= re.sub(r"\D", "*",  ip3)
print(updatedip3)

import re
ip3 = "my num is 856429875"
updatedip3= re.sub(r"5", "*",  ip3)
print(updatedip3)

# spilt - splits the string whenever the patter matches
import re
eg = "apple,banana,mango"
op = re.split(",", eg)
print(op)