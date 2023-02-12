def LMS():
    print("BOOKS")
    print("Student")
    print("Staff")
    print("Author")
LMS()


print("__________With Arguments_________________")
def avg(x,y):
    
    print("Average of",x,"and",y,"is",(x+y)/2)
avg(3,8)

print("__________Without Arguments_____________")
def avg():
    x=0
    y=0
    print("Average of",x,"and",y,"is",(x+y)/2)
avg()


######################           CWH              #########################
a=9
b=8
gmean1=(a*b)/(a+b)
print(gmean1)
c=90
d=80
gmean2=(c*d)/(c+d)
print(gmean2)


#For above code written two time thats why function is used
def gmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
a=9
b=8
gmean(a,b)
c=90
d=80
gmean(c,d)

###########################################
a=90
b=10
if(a>b):
    print("a is greater")
else:
    print("b is greater or equal")
c=90
d=80
if(c>d):
    print("c is greater")
else:
    print("d is greater or equal")
################################################
def isGreater(d,e):
    if(d>e):
        print("First num is greater")
    else:
        print("2nd num is greater or equal")
def isLesser():
    pass   #It means it will be write afterwards so just pass this fn
d=90
e=10
isGreater(d,e)
f=90
g=800
isGreater(f,g)



######################With ARgumnets###############
###################DEFAULT ARGUMENTS############
def average(a=10,b=20):
    print("The average of a and b is " ,(a+b)/2)
average()
#########################
def average(a,b):
    print("The average of a and b is " ,(a+b)/2)
average(8,9)
#########################
def average(a=10,b=20):
    print("The average of a and b is " ,(a+b)/2)
average(80,90)           #Above arguments will be ignored
############KEYWORD ARGUMENTS##############
def average(a=10,b=20):
    print("The average of a and b is " ,(a+b)/2)
average(b=20,a=90)  #oredred of a and b can be changed
#################Required Arguments ###############
def average(b,a=10):
    print("The average of a and b is " ,(a+b)/2)
average(9)

############ARBITRARY ARGUMENTS(Variable length Arguments)###########
def average(*numbers):    #Numbers will be taken as tuple
    sum=0
    print(type(numbers))   # it will give tuple
    for i in numbers:
        sum=sum+i
    print("Average is:",sum/len(numbers))
average(5,6)
average(5,6,8,9,6,5,7,10,80)

############################################
def average(*numbers): 
    sum=0 
    for i in numbers:
        sum=sum+i
    #return 7   #first return will be taken and afterwards return will be ignored means return statement is used to return the value of the expression back to the calling fn
    return sum/len(numbers)
c=average(50,6,200)
print(c)
