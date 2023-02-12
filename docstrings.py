#Docstring is not ignored like a comment

def square(n):
    '''Takes in a number n,returns the square of n'''   #Docstring shoul be always written just below the function and above the body,in between should not be anything for valid docstring
    print(n**2)
square(5)
print(square.__doc__)# by changing comment u cant change the output of a program but by chnging docstring u can change the output of a program

##############         PEP8 = Python Enhancement Proposol         ##############

