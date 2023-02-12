class Parent1:
    def assign_string_one(self,str1):
        self.str1=str1
    def show_string_one(self):
        return self.str1
class Parent2:
    def assign_string_two(self,str2):
        self.str2=str2
    def show_string_two(self):
        return self.str2

class Child(Parent1,Parent2):
    def assign_string_three(self,str3):
        self.str3=str3
    def show_string_three(self):
        return self.str3
my_child = Child()
my_child.assign_string_one("I m string of parent1")
my_child.assign_string_two("I m string of parent2")
my_child.assign_string_three("I m string of child")
print(my_child.show_string_one())
print(my_child.show_string_two())
print(my_child.show_string_three())
