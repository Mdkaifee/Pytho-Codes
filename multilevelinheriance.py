class Parent:
    def get_name(self,name):
        self.name=name
    def show_name(self):
        return self.name
class Child(Parent):
    def get_age(self,age):
        self.age=age
    def show_age(self):
        return self.age
class GrandChild(Child):
    def get_gender(self,gender):
        self.gender=gender
    def show_gender(self):
        return self.gender

gc=GrandChild()
gc.get_name("Amit")
gc.get_age(202)
gc.get_gender('feMale')
print(gc.show_name())
print(gc.show_age())
print(gc.show_gender())