for char in "Python":
    if (char=="o"):
        break
    print(char)
print("")
###########################
for char in "Python":
    if (char=="o"):
       continue
    print(char)
print("")
###########################
for char in "Python":
    if (char=="o"):
       pass
    print(char)

#########################
for i in range(12):
    if (i==10):
       break              #breaking out of the loop
    print("5 X", i+1 ,"=",5 * (i+1))
    
print("came out of loop")


######################################
for i in range(12):
    if (i==10):
       print("Skip the iteration")
       continue
    print("5 X", i ,"=",5 * (i))
