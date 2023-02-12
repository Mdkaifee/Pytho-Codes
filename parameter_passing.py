
'''
l=[100,200,300]
l.append(600,800)  #Two items appending at a time will gives an error so u need to do by function
print(l)
'''
#******************Variable Length positional args***********
'''

def add_value(*args):  #it become tuple so u can access these below items
    print(args)
add_value(100,200,300,400,500)
add_value(100,200)
add_value(100,200,300,400,500,600,700,800)
'''
def add_value(*args):  #*args pass all the value as a tuple
    l=[]   #Now it becomes list and can access any element
    for value in args:
        l.append(value)
    return l
   
result=add_value(100,200,300,400,500)
print(result)

result=add_value(100,200)

result=add_value(100,200,300,400,500,600,700,800)
print(result)
#******************Variable Length keywords args***********


#name,email,contact,dob
def get_details(**kwargs):  #**kwargs  pass all the value as a dictionary
    print(kwargs)
get_details(name="ABC",email="abc@gmail.com",contact=788965486,dob="12-11-2022")
get_details(name="ABC",email="abc@gmail.com",dob="12-11-2022")
get_details(name="ABC",contact=788965486,dob="12-11-2022")

