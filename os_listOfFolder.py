import os
folders=os.listdir("data")
print(folders)   # IT WILL TELL ME and print THE TOTAL FOLDER AVAILABLE IN data folder

print("")

for folder in folders:
    print(folder)  #for printing folder horizontally
    print(os.listdir(f"data/{folder}"))  #This will tell the content in each folder

    print("")
#print(os.getcwd())    #It will tell you the dircetory
#os.chdir("/Users")  #It will be used to change the dircectory from previous existed dir to users
#print(os.getcwd())   Here changes can be seen
#os.remove()  #Removes a file
#os.rmdir()  #Removes an empty directory
#shutil.rmtree #Deletes a directory and all it's content