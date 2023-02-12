x=10


def hello():
    global x   #global x will change now into global var
    x=4 
    y=5          
    print(y)
     
hello()

print(x)
#print(y)   # IT will give error because it is a local var for making it global it should be written like 