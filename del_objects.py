class car:
    def __init__(self,name,color,model):
        self.name=name
        self.color=color
        self.model=model
c1=car("ford","white",2020)
c2=car("ford","white",2020)
c3=car("ford","white",2020)
print(c1.name,c1.color,c1.model)
print(c2.name,c2.color,c2.model)
print(c3.name,c3.color,c3.model)
del c1.name
del c2   #It is not possibe to delete all obj of c2
print(c1.color,c1.model)
print(c2)