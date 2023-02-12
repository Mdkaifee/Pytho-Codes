import math
print(math.floor(4.2536))
print(math.sqrt(9))
from math import sqrt,pi     #It only import two math fn from whole math module
print(sqrt(9))
#print(math.floor(4.2536)) it will through error because u are just importing sqrt and pi from math
print(sqrt(9)* pi) 

from math import *  #Importing all the fn and variables from a module using * without wildcard,it is little bit confuse bcz we dont know from where the var and fn is coming
print(sqrt(9)* pi) 
print(pi)


########## as keyword=short form ##########
#example:import panda as pd
import math as s
print(s.sqrt(9) * s.pi)
print(s.pi)
import math as m
print(m.sqrt(9) * m.pi)
print(m.pi)


############             DIR           ###############
#If u dont know about any module then by using dir u will get all the built in fn & var available in that module which u r importing
import math
print(dir(math))     # All the fn will be printed which is available in math

#Python also allows u to rename module   
from kaifee import welcome,md    #It will import welcome fn and md variable

welcome()   #calling a fn from another kaifee module
print(md)    # Printing variable md and Here i m importing a module written by me whose name is kaifee.py

from kaifee import *    #From kaifee everything will be imported
welcome()
print(md)

import kaifee as hr
hr.welcome()
print(hr.md)