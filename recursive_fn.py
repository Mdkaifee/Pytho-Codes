#Factorial fo a number
'''
def factorial(num):
    if num==1:
        return 1
    else:
        return num*factorial(num-1)
num1=5
result=factorial(num1)
print(result)
'''
#BINARY SEARCH
def bSearch(l,key):

    if len(l)==0:
        return False
    else:
        
        mid=len(l)//2
        if l[mid]==key:
            return True
        elif key<l[mid]:
            return bSearch(l[:mid],key) 
        else:
            return bSearch(l[mid+1:],key) 

l=[10,20,30,40,50,60,70,80,90]
key=700

result=bSearch(l,key)
print(result)
