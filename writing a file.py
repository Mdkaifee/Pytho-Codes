f=open('myfile2.txt','w') 
f.write('Hello,world!') 



f=open('myfile2.txt','a') #In append mode whatever u have already written  in file will be added to the last
f.write('Hello,world!') 
f.close()   # A good habit to use


#  When you don't want to write close then it will take automatica close by using this syntax
with open('myfile2.txt','a') as f:
    f.write("Hey I am inside with")