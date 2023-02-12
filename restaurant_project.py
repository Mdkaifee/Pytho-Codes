#key: customer name, value: $ budget
cust_dict = {
  "Alice":50,
  "John": 12
}

#key: meal, value: meal price
menu_dict = {
  "burger": 8,
  "pizza": 14,
  "cake": 5
}

taxes = 0.8

def welcome(customer,budget):
  #multi-line print statment
  print(f"Welcome to our Resturant! {customer}, Budget:{budget}")
  print("---------------------------------")
  print("Menu List:")
  for meal,price in menu_dict.items():
    print(f"{meal} costs : {price}")
  print(f"Taxes : {taxes}")
  

def calculation(customer,budget):
  budget = budget#int(input("Your Budget ? : "))
  meal = input("What would you like to have ? : ").lower()

  while meal not in menu_dict.keys():
    print(f"{meal} is not available, try again.")
    meal = input("What would you like to have ? : ").lower()

  meal_price = menu_dict[meal]

  while meal_price + taxes > budget:
    print(f"sorry no enough budget for {meal}.")
    meal = input("What would you like to have ? : ").lower()
    meal_price = menu_dict[meal]


  left_budget = (budget - meal_price) - taxes

  print(f"Meal price : {meal_price}, Taxes : {taxes}")
  print(f"Your Left Budget is {left_budget}, Thank you for choosing us Dear {customer} :).")
  print("")


for customer,budget in cust_dict.items():
  welcome(customer,budget)
  calculation(customer,budget)
