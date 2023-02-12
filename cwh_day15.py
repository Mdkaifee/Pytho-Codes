import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
timestamp=time.strftime('%H')
print(timestamp)
timestamp=time.strftime('%M')
print(timestamp)
timestamp=time.strftime('%S')
print(timestamp)


##########        Looping        ###########
#Print natural number using for loop
for i in range(9):#for i in range(1,9)://for i in range(1,9,2):
    print(i)
######################################
num=10
for i in range(1,num+1):
    print(i)

###############################
name='Abhishek'
for i in name:
    print(i)
    if(i=="b"):
        print("B IS FOUND")

#################################
colors=["Red","White","Black"]
for color in colors:
    print(color)
    for i in color:
        print(i)

#################################
#############        While Loop        ##########
i=1
while (i<5):   #1234
    print(i)
    i=i+1
############################################
i=5
while (i>0):
    print(i)       #54321
    i=i-1
########################################
i=5
while (i>0):
    print(i)    #54321
    i=i-1
else:
    print("I'm else")
#######################################

