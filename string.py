s1=str("Hello")
for chr in range(0,2):
    print(s1[chr])

name="Kaifee"
car_color="red"
print("Hello world,my name is"
    +" "+ name +" "+",and my car color is"+" "+car_color)
msg="Hello world,my name is Kaifee ,and my car color is red"
print(len(msg))
print(len(name))
print(len(name[0:4]))
print((name[0:4]))




#**************#

message='This is user car'
print(message.count('r'))
print(message.count('r',5))#in order to count from index 5 to end of string
print(message.count('s',5,12))#in order to count from index 5 to 12
print(message.count('T'))
print(message.count('U'))
print(message.count('u'))

#*******Endswith********#

text='user_car'
x=text.endswith("car")#Check if a string contain specific suffix like car
print(x)
y=text.endswith("user",4)#check from index 4 to end of srtring
print(y)
z=text.endswith("car",4,8)
print(z)
t=text.endswith("car",5,7)
print(t)
k=text.endswith(("car",'ar'),4,8)
print(k)

#***********Find()***************
mess='This is user_car'
a=mess.find('i')        #it will tell us the number of i in a string
print(a)        
#***************Where in the text is the first occurrence of the letter "e"?:****************
txt = "Hello, welcome to my world."
x = txt.find("e")
print(x)
#*******Where in the text is the first occurrence of the letter "e" when you only search between position 5 and 10?:***********************
txt = "Hello, welcome to my world."
x = txt.find("e", 5, 10)
print(x)
#*********************If the value is not found, the find() method returns -1, but the index() method will raise an exception:******************+
txt = "Hello, welcome to my world."
print(txt.find("q"))
#  print(txt.index("q"))          THIS WILL GIVE VAULUE ERROR

#*************************#
txt='This is User Car'
x=txt.upper()
Y=txt.lower()
print(x)
print(Y)
################*********The capitalize() method returns a string where the first character is upper case, and the rest is lower case.**********###################
txt = "python is FUN!"
x = txt.capitalize()
print (x)

################*****See what happens if the first character is a number:******######################

txt = "36 is my age."
x = txt.capitalize()
print (x)



###############**********Make the lower case letters upper case and the upper case letters lower case:********########################

txt = "Hello My Name Is PETER36"
x = txt.swapcase()
print(x)


##############***********Make the first letter in each word upper case:***********#############

txt = "Welcome to my world 2nd"
x = txt.title()
print(x)


################*********************#########################
txt = "hello b2b2b2 and 3g3g3g"
x = txt.title()
print(x)


#################*****Joining the string***************#################
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)             #The fn that return a string is joined by a separator,here in this case # is used,u can use a dot here too
print(x)

##########################*******************REPLACE***************#################################
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

##############**************Replace the two first occurrence of the word "one":**********##############

txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three", 2)
print(x)

##############************Remove spaces at the beginning and at the end of the string:************##############

txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")

##############************Remove the leading and trailing characters:************##############

txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")
print(x)
print("")

#Strings are immutable and ex are:-----can't modify the string at the same memory location,new memory location will be form if u create new variable-------
z1="Hello world"
print(id(z1))

z1="java"
print(id(z1))
print("")

#---------String slicing-----------
t="Python is really fun"
print(t[0:5])  #strts 0 to 6
print(t[6:])   #6 to end
print(t[:6])   #default strt with 0
print("")

#----------String striding------------
print(t[::2])
print(t[2::])
print(t[::])
print(t[::-1])    #reversing the string
print(t[::-2])    #every second char will reverse from ryt side
print(t[6:0])    #empty space
print("")

#---------------------------------------#
u1 = "I m a student"
for value in u1[::2]:
    print(value)
print("")

#------------It gives u all the built in fn in string-------------------#
#help(str)

#-------------It gives you the various fn u can apply on string
print(dir(str)) 
