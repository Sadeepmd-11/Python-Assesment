#Question 35

class Vehicle:
    def __init__(self, brand):
        self.brand=brand

    def fuel_type(self):
        return self

class ElectricCar(Vehicle):
    def fuel_type(self):
        return "Electricity"
    
c=ElectricCar("Tesla")
print(f"Brand: {c.brand}")
print(f"Fuel_type: {c.fuel_type()}")

#-------------------------------------------------
#Question36
class bankaccount:
    def __init__(self, balance):
        self.__balance=balance

    def deposit(self,amount):
        self.__balance+=amount
        print(f"deposited {amount}")
        print(f"balance is {self.__balance}")
    
    def withdraw(self, amount):
        if amount > self.__balance:
            print(f"Insuffeciat balance! balance amount is {self.__balance}")
        else:

            self.__balance-=amount
            print(f"withdraw amount={amount}")
            print(f"balance={self.__balance}")


account=bankaccount(100)
account.deposit(50)
account.withdraw(200)
print("")

#-------------------------------------------------------------------
#Question37

class Student:
    def __init__(self, name):
        self.name=name
        self._score= 0

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        if value>=0 | value <=100:
            self._score=value
        else:
            print("score must be b/w 0 to 100")

s=Student("Kevin")
s.score=105
