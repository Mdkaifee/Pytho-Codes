f=open('myfile.txt','r')           #It's a read mode and u can't write and it's default mode and u can or cant give mode argument
print(f)     #file will be open


###########      Reading a file      ##########
text=f.read()
print(text)    
f.close()        # Closing a file  

f=open('myfile2.txt','w')     # It will create a file name myfile2(If a file doesn't exist and try to open in write mode then a file will be formed)

#If i want to add content in a file the we use append mode 

#f=open('myfile.txt','rt')    Opening a file in text mode

#f=open('myfile.txt','rt')    Opening a file in binary mode

