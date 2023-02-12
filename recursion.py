############ Facorial ############
#factorial(7)=7*6*5*4*3*2*1
#factorial(6)=6*5*4*3*2*1
#factorial(5)=5*4*3*2*1
#factorial= n * factorial(n-1)
def factorial(num):
    if (num == 0 or num==1):
        return 1
    else:
        return num * factorial(num-1)
print(factorial(5))

############# Fibonacci ############
#f(0)=0
#f(1)=1
#f(2)=f(1)+f(0)
#f(n)=f(n-1)+f(n-2)


def fibonacci(num):
    if (num==0 or num==1):
       return num
    else:
        return fibonacci(num-1)+fibonacci(num-2)
print(fibonacci(6))