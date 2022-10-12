#Parent class 


class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def show_details(self):
        print("User details")
        print("")
        print("Name ",self.name)
        print("Age ", self.age)
        print("Gender ",self.gender)


#Child Class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Account balance has been updated: ", self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("You have insufficient Funds | Available balance is: $",self.balance)
        else:
            self.balance = self.balance - self.amount
            print("You have withdrawn $",self.amount)
            print("Your available balance is $",self.balance)

    def view_balance(self):
        self.show_details()
        print("Your available balance is $",self.balance)
