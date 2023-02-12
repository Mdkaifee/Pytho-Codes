'''def concat(val1,val2):
    return val1+val2

result=concat(10,10)
print(result)

result=concat("python","fun")
print(result)

result=concat("10","fun")
print(result)

#THIS BELOW STATEMENT WILL GIVE AN ERROR THAT'S WHY DECORATOR IS USED
result=concat(10,"fun")
print(result)
'''
def deco(func):
    def new_func(val1,val2):
        if type(val1)==type(val2):
            return func(val1,val2)
        else:
            return func(str(val1),str(val2))
    return new_func
@deco
def concat(val1,val2):
    return val1+val2

result=concat(10,10)
print(result)

result=concat("python","fun")
print(result)

result=concat("10","fun")
print(result)

#THIS BELOW STATEMENT WILL GIVE AN ERROR THAT'S WHY DECORATOR IS USED
result=concat(10,"fun")
print(result)


