'''class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
obj=person("Kaifee",22)

print(obj.name)
print(obj.age)
'''
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def hi(self):
        print("Hi, my name is "+self.name) #OBJECT METHOD
obj=person("Kaifee",22)
obj.hi()

#print(obj.name)
#print(obj.age)