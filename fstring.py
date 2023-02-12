#Used to format string

letter="Hey my name is {} and i m from {}"
country="India"
name="Kaifee"
print(letter.format(name,country)) # it will works order wise first bracket will take name and other country

##############################################
letter="Hey my name is {1} and i m from {0}"
country="India"
name="Kaifee"
print(letter.format(name,country)) # it will works order wise 0 will take name and 1 will take  country

#For doing this we have to write enough so short cut method is fstring bcz it is used to avoid numbering
country="India"
name="Kaifee"
print(f"Hey my name is {name} and i m from {country}")

print(f"Hey my name is {{name}} and i m from {{country}}")     #  If dont want any replace as an argument 

#################################################
price=49.0999
text=f"For only {price:.2f} dollars!"    #It will just take 2 decimal point
print(text)

##################
print(f"{2*30}")
print(type(f"{2*30}"))
