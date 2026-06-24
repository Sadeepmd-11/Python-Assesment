#1.Basic List operation

##Creating list and prinitng
cars=["audi", "bmw", "benz"]
print(cars)

##Accesing the elements in the list
print(cars[1])
print(cars[-2])

##Appending the item to the list
cars.append("suzuki")
print(cars)

##Deleting the item in the list using pop and remove
cars.pop()
print(cars)
cars.append("suzuki")
cars.remove("suzuki")
print(cars)

##Adding the item in particular index of the list 
cars.insert(2,"hyundai")
print(cars)

##Replacing the item in the list
cars[2]="tata"
print(cars)

##printing the length of the list
print(len(cars))