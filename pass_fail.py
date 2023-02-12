math=int(input("Enter math marks:"))
chemistry=int(input("Enter chemistry marks:"))
physics=int(input("Enter physics marks:"))
eng=int(input("Enter eng marks:"))
hindi=int(input("Enter hindi marks:"))
total=(math+chemistry+physics+eng+hindi)/5
print("Marks in percent=",total)
if(total>=90):
                print("Student got the distinction")
elif total>=80 and total<90:
   print("Student got the first division")
elif total>=70 and total<80:
    print("Student got the second division")
elif(total>=60 and total<70):
    print("Student got the third division")
else:
     print("Student got fail")
