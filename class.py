'''
class phone:
    def make_call(self):
        print("I am making call")
    def play_game(self):
        print("I am playing game")
p1=phone()
p1.make_call()
p1.play_game()
'''
class phone:
    def set_color(self,color):
        self.color=color
    def set_cost(self,cost):
        self.cost=cost
    def show_color(self):
        return self.color
    def show_cost(self):
        return self.cost
    def make_call(self):
        print("I am making call")
    def play_game(self):
        print("I am playing game")

p2=phone()
p2.set_color("blue")
p2.set_cost(5000)
p2.show_color()
p2.show_cost()
p2.make_call()
p2.play_game()