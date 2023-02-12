def greetings():
    print("Hello world")
greetings()
def greetings(user):
    print("Hello world")
greetings("adam")
def greetings(user,age):
    print("Hello " + user + ",you are " +str(age)+ " years old")
greetings("adam",20)
print("")

#############Example1#################
def my_function(fname):
    print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")
print("")

###################Example:This will give error:no of argumnets not matched****************************
'''
def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil")
'''

##############Example2:If the number of arguments is unknown, add a * before the parameter name:This way the function will receive a tuple of arguments, and can access the items accordingly:*****************######################
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")
print("")

#********************You can also send arguments with the key = value syntax .This way the order of the arguments does not matter.******************
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
print("")
############################EXAMPLE:INFINITE ARGUMENTS#########################
def print_people(*people):
    for person in people:
        print("This person is",person)
print_people("Nick","Richa","Daniel","Hezel","Smiley")
print("")

######################RETURNING FUNCTION####################
def calculation(a,b,c):
    print(a+b+c)
    print("This is a calculation")
    return print(a-b-c)
    print(a*b/c)        #outside return
    print("something")  #outside return
calculation(1,2,3)