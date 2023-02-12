'''for i in range(5):
        print ("HI " +str(i))
'''
'''
for i in range(1,5):
        print ("HI " +str(i))
'''
'''
for i in range(2,13,2):
        print ("HI " +str(i))
'''
for i in range(1,13,2):   #Iterable datatypes in python are str,list,dict,set,tuple
    if(i==3):
        continue
    print (i)
print("")
#######################Iteration########################
l=[10,20,30,40,50]
for value in l:
        print(value)
print("")
##############Addition of all element##################
x=[1,2,3,4,5]
sum=0
for value in x:
        sum=sum+value
        print(sum)     #this print is inside for loop so print every time it will add
print("")       
print(sum)