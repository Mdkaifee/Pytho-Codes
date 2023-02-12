from re import T

from numpy import char


def value_reverse(value):
    reverse=value[::-1]
    print(reverse)

s="Python"
result =value_reverse(s)
print(result)      #It will give None

#**********************Reversing a list*****************
l=[100,200,300,400]
result =value_reverse(l)
print(result)

'''*******Slicing will not work on integers**********#In this typecast the int into string

num=100
result=value_reverse(num)
print(result)
'''

#************Argunments in Function**************

#*************************1.Positional argument:if total number of function name and function definition are same then is called positional argumnet*************************************

def linear_search(l1,key):
    for value in l1:
        if key==value:
            return True
        else:
            return False

l1=[100,200,300,400,500]
key=4000
result=linear_search(l1,key)   #Here u cant pass one or three argument
print(result)

#****************Defaualt Argument************

import random
def gen_password():

    l=['@','#','$','&']
    upper=chr(random.randint(65,90))
    lower=chr(random.randint(97,122))
    special=random.choice(l)
    digit=random.randint(10000,99999)
    password=upper +lower+special+str(digit)
    return password

result=gen_password()
print(result)

#****************Keyword Argument*************

def validate(username,password):
    if username=="ABC" and password=="ABC@123":
        print("valid password")
    else:
        print("invalid password")
validate("abc123","ABC@123")
validate("ABC","ABC@123")
validate("ABC@123","ABC")
validate(password="ABC@123",username="ABC")


#******************New Thing**************
print(100,200)
print("Hi")
print(100,200,sep=",",end=" ")
print("Hi")