clients ={"adam":"01111","John":"02222","mike":"033333"}  # Duplicacy not allowed like "mike"="156589" then that will print shich is at last
print(clients)
print(clients["adam"])
print(len(clients))
#############################################
for i in clients.keys():#Instead of key here u can use values then number will print
    print(i)
##############################################
if "elice" in clients.keys():
    print("found")
else:
    print("Not found")
##########################################
if "01111" in clients.values():
    print("found")
else:
    print("Not found")
###########################################
clients["alice"]="055636"        #For adding element in dictionary
print(clients)
################################33
del clients["adam"]              #For deleting element feom dictionary    or u can do clients.pop["adam"] 
print(clients)
##########################################

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
####################dictionaries are defined as objects with the data type 'dict':---------     <class 'dict'>###############################
print(type(thisdict))
x = thisdict.get("brand")    #thisdict.get("Baleno") then it'll print none instead of ford
print(x)

#####################################################
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()     #Here car.keys can also be used for the key values only
print(x) #before the change
car["year"] = 2020
print(x) #after the change
'''
del car      #this will cause an error because "thisdict" no longer exists.
print(car)
'''
#############The clear() keyword empties the dictionary:#################
car.clear()
print(car)

