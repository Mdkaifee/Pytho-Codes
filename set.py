set1={1,"male",2,3,4,5,4,3,1}   #Duplicate values will be ignored:
print(set1)
#print(set1[0])    You can't do like this because for accessing it we need to use for loop

print(type(set1))#type of datatypes

print(len(set1))     #will tell the Length of the sets

set1.add(6)          #For adding 
set1.remove(3)       #For removing       ********discard can be also used in place of remove
print(set1)

#Remove the last item by using the pop() method:
c=set1.pop()
print(c)             #removed item
print(set1)          #the set after removal

#Accessing items
set2={"apple", "banana", "cherry"}
for i in set2:
    print(i)#Duplicate or repeated number is printing only once

#Check if "banana" is present in the set using in:true/false
print("banana" in set2)

#ADDING TWO SETS:Add elements from set2 into set1:
set1={1,"male",2,3,4,5,4,3,1}
set2={"apple", "banana", "cherry"}
set1.update(set2)
print(set1)

#Add Any Iterable:The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
set1={1,"male",2,3,4,5}
mylist=["apple", "banana", "cherry"]
set1.update(mylist)
print(set1)

#converting set into list
list1=[1,1,2,2,3,3,4,4]  
set1=set(list1)
list1=list(set1)
print(set1) 
print(list1)

#The clear() method empties the set:
set1.clear()
print(set1)
#####################    UNION     ##############
s1={1,2,3,4,5}
s2={8,9,10,5}
print(s1.union(s2))

####        INTERSECTION       ################
print(s1.intersection(s2))       

####        DIFFERENCE       ################
print(s1.difference(s2))  
print(s2.difference(s1))   

####        DISJOINT       ################
print(s2.isdisjoint(s1))      # If two sets having atleast one same element then it will give false if no matching in 2 set on which disjoint is applying then it will give TRUE

####        SUPERSET       ################
print(s2.issuperset(s1))

####        SUBSET       ################
print(s2.issubset(s1))
