import math
price=int(input('Enter the value of product:'))
cgst=int(input('Enter the value of cgst in percent:'))
sgst=int(input('Enter the value of sgst in percent:'))
total=price+((cgst*price)/100)+((sgst*price)/100)
print('New product price=',total)