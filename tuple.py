#Same as lists but tuples are unchangeable means u can't do delete,update,and insert and use of paranthesis here 
tuple1=(1,2,"Hello","aPPLE","CHERRY")   #Tuple allows duplicate values
print(tuple1)
print(tuple1[2])
print(tuple1[-1])
print(tuple1[-3:-1])
print(tuple1[1:3])
print(tuple1[:2])
print(tuple1[2:])

#tuple[1]=0  #can't do this in tuple like lists
 
list1=list(tuple1)  #Now it will traet as lists
print(list1)
list1[1]=0  #Here reflect the changes
print(list1)

#Add tuple to a tuple WITHOUT CONVERTING INTO LISTS
y=("KAIFEE",)
tuple1 += y
print(tuple1)

#Multiply the tuple by any number
tuple1=2*tuple1

# del tuple     It will delete the tuple and error will be thrown afterwards

#For removing an item from a tuple(Convert into a list,remove then make tuple again)
z=list(tuple1)
z.remove("CHERRY")
tuple1=tuple(z)
print(tuple1)

print(len(tuple1))   # TELL us abt the length of the tuple

thistuple = ("apple",)    #EXAMPLE OF TUPLE
print(type(thistuple))
 
thistuple = ("apple")     #EXAMPLE OF STRING NOT TUPLE
print(type(thistuple))


#To determine if a specified item is present in a tuple use the in keyword
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")


