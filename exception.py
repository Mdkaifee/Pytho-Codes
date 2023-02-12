import sys
#ValueError     int("abc")
#IndexError     a=["a","b"]
#               a[5] ****Index [5] is not available
#keyError
#zeroDivisonError    5/0
print("")
print("_______________________________")

x=int(input("Enter the value of x="))
y=int(input("Enter the value of y="))
try:
    z=x/y
except:
    print("Division by zero is not possible")
    print("Exception",sys.exc_info())
else:
    print(z)

print("")
print("--------------------------")

r=[1,2,5,9,'j',0]
for i in r:
    try:
        l=1/i
    except:
        print("Exception",sys.exc_info()[0])
    else:
        print(l)


#ValueError
#IndexError

try:
    l=[1,5,6,8]
    i=int(input("Enter index:"))
    print(l[i])
except:
    print("Please Enter a valid index")
finally:
    print("Execution completed")#it can  execute without using finally but while u write in function then you can face difficulty because even after return if u want that to execute that's why finally is used


#########    Real use of word finally   ##########
def func1():
    try:
     l=[1,5,6,8]
     i=int(input("Enter index:"))
     print(l[i])
     return 1    #even after returning the execution of the program will go till the the finally
    except:
       print("Some error occured")
       return 0
    finally:
       print("I am always executed")
x=func1()
