marks=[22,35,98,56,11,4,8,9]
index=0
for mark in marks:
    print(mark)
    if (index==3):
        print("SUUUUUUUuuuuuuuuuIIIIIIII")
    index+=1
print("")

#############################################
#Above code can be write like this using enum

marks=[22,35,98,56,11,4,8,9]
for index,mark in enumerate(marks):
    print(mark)
    if (index==3):
        print("SUUUUUUUuuuuuuuuuIIIIIIII")
   
print("")

#######################################
marks=[22,35,98,56,11,4,8,9]
for index,mark in enumerate(marks,start=3):
    print(mark)
    if (index==3):
        print("SUUUUUUUuuuuuuuuuIIIIIIII")
   
print("")

fruits=['apple','banana','mango']
for index, fruit in enumerate(fruits):
    print(index,fruit)