class cars():
    def __init__(self):
        self.name="BMW"
    def show_detail(self):
        print(self.name)

class BMW(cars):
    def __init__(self):
        self.name="This is my BMW Car"
    def show_detail(self):
        print(self.name)
c=cars()
c1=BMW() # Here two objects are created c and c1
c.show_detail()
c1.show_detail()
