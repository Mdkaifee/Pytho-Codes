f=open("untitled.txt","r") #File name is:hi.text whatever written will be in file will be in output for reading,r(default),rb(binary form),rt can also be used after writing file name
print(f.read())  #if i m writing f.read(3) then only three character will show on output screen
print(f.readline())#FIRST LINE will be printed in output     #if i m writing f.readline(3) then only three character will show on output screen
f.close()
'''
f=open("untitled.txt","r")
for x in f:
    print(x)
'''