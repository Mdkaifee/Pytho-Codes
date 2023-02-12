#List is a collection datatypte,it's a collection of values,those values are called items nd they are separated by comma.
#Ordered and changeable items,we can add,update and delete items   ex:List1=[10,"Hello",5.5,True]
list1=[10,"Hello",5.5,True]
print(list1)
print(list1[-1])
print(list1[3])
list1.append(29)#Append function for inserting an element in lists
print(list1)
list1.remove(True)#remove function for removing an element in lists
print(list1)
list1[0]=5
print(list1)
for i in list1:
    print(i)
