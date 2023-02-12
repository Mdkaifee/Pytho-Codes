#WIthout comprehension
'''
l=[100,200,300,400,500]
l2=[]
for value in l:
        l2.append(value*value)
print(l2)
'''
########################################
print("With comprehension :  used if u want to perform operations on each element")
l=[100,200,300,400,500]
l2=[value*value for value in l]
print(l2)

#############################################
print("Output should be comes only even number")
l=[101,200,3003,400,5200]
l2 =[value for value in l if  value%2==0]
print(l2)

##############################################
l=['abc','abcd','abcde','abcdef']
l2=[len(value) for value in l]
print(l2)

###########################################
l=[[1,2,3],[9,4,5],[0,6,7]]
print(l)

########################################
print("Done without comprehension")
l=[[1,2,3],[9,4,5],[0,6,7]]
#l2=[]
for value in l:
        for values in value:
                print(values)

############################################
print("Done with comprehension")
l=[[1,2,3],[9,4,5],[0,6,7]]
l2=[values for value in l for values in value]
print(l2)

#########################################
print("")
print("Even and odd by comprehension")
l=[101,200,3003,400,5200]
l2=["Even" if value%2==0 else "Odd" for value in l]
print(l2)
############################################
print("")
print("Dictionary comprehension")
d={x*x for x in range(1,11)}
print(d)
#######################################
print("")
d={x:x*x for x in range(1,11)}
print(d)
######################################
print("")
d={chr(x) for x in range(97,123)}
print(d)
####################################
print("")
d={chr(x):x for x in range(97,123)}
print(d)
print("")
#####################################
print("Swap keys & values in existing dictionary")
d={chr(x):x for x in range(97,123)}
d2={value:key for key,value in d.items()}
print(d2)
