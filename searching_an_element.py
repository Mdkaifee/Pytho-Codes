x=[10,20,30,40,50,60]
key=400
for value in x:
    if value==key:
        print("Element found")
        break
    else:
        continue    #pass
        print("Hiiiiiiiiiiiiii KAIFEE")    #this piece of code will never run because just looking the continue statement python jst skip all tha thing written after that and go for the nxt iteration but it can be reached by using pass statement instead of continue here
else:      #it is an optional else block,run if element will not found
    print("Element not found")
print("")

#####################If u want to know about the position of the value present######################
z=[1,2,3,4,5,6,7,8,9]
for index,value in enumerate(z):
    print(index,value)
print("")

#############SEARCH ELEMENT BY TELLING THE POSITION#########
l=[10,20,30,40,50,60]
key=40
for index,value in enumerate(l):
    if value==key:
        print("Element found at index",index)
        break
    else:
        continue
else:      #it is an optional else block,run if element will not found
    print("Element not found")