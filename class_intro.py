class account:
    def __init__(self,cust_id,name,initial_balance=0):
        self.id=cust_id
        self.name=name
        self.balance=initial_balance

    def get_balance(self):
        return self.balance

    def deposit(self,amount):
        self.balance=self.balance+amount
        return self.balance
    
    def withdraw(self,amount):
        if amount>self.balance:
            return "Insufficient funds"
        else:
            self.balance=self.balance-amount
            return self.balance

customer1=account("101","ABC")

customer2=account("102","XYZ")

print(customer1.get_balance())
print(customer1.deposit(5000))
#print(customer2.get_balance())
print(customer1.withdraw(4000))  #If u will take 6000 then insufficient funds will come in output
customer3=account("103","PQR")
#print(customer1)


