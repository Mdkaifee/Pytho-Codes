class car:
    name="Ford"
    color="white"
    model=2020
    def display(self):
        print(self.name)
        print(self.color)
        print(self.model)
c=car()
print(getattr(c,"name"))
print(getattr(c,"color"))
print(getattr(c,"model"))
print(hasattr(c,"name"))   #It will give true due to presence of object
print(setattr(c,"name","Toyota"))
print(c.name)   #Updated here
print(getattr(c,"color"))
print(getattr(c,"model"))
print(c)
print(getattr(c,"name"))
print(delattr(c,"name"))   #Here updated name will be deleted
print(c.name,c.color,c.model)   #After deletion old name will be shown here