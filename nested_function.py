def outerfunction():
    print("Hello,i am outer fn")
    def innerfunction():
        print("Hello,i am inner fn")
    innerfunction()
outerfunction()

print("___________________________")

def num(x):
    def num1(y):
        return x*y
    return num1
result=num(20)
print(result(2))