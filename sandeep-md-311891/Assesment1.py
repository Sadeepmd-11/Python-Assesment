#1.Basic List operation

##Creating list and prinitng
cars=["audi", "bmw", "benz"]
print(f"printing the list={cars}")

##Accesing the elements in the list
print(f"accesing the element= {cars[1]} ")
print(f"accesing the element= {cars[-2]} ")

##Appending the item to the list
cars.append("suzuki")
print(f"adding the element at end of list = {cars}")

##Deleting the item in the list using pop and remove
cars.pop()
print(cars)
cars.append("suzuki")
cars.remove("suzuki")
print(cars)

##Adding the item in particular index of the list 
cars.insert(2,"hyundai")
print(f"adding the new element to list={cars}")

##Replacing the item in the list
cars[2]="tata"
print(f"replacing the item={cars}")

##printing the length of the list
print(f"length of the list={len(cars)}")

#2.List Manipulation

##Adding the multiple elements in the list
cars.extend(["mahindra", "toyota"])
print(f"extended list={cars}")

#3.Sum and Average of the numbers in the list

##Sum of the Numbers
num=[1,5,2,7]
sum=0
for i in num:
    sum+=i
print(f"sum of numbers in list = {sum}")

##Average of the numbers
average=sum/len(num)
print(f"average = {average}")

#4.Reverse of list
num.reverse()
print(f"reverse of list = {num}")

#5.Square of the number
num2=[x**2 for x in num]
print(f"square os the number in the list= {num2}")

#6.Max and Min of the list
maxi=max(num)
print(f"maximum of the list = {maxi}")
mini=min(num)
print(f"minimum of the list = {mini}")

#7.count occurances
num3=[1,1,2,3,3,4,2,4]
occ=int(input("enter a number for count b/w 1-4: "))
occurnce=num3.count(occ)
print("occurance=", occurnce)

#8.sort a list of numbers.
num3.sort()
print("sorted number=", num3)


#9.copy a list
new_list=num3.copy()
print("copied new_list=", new_list)

#10.combine two list
n1=["a","bc","de"]
n2=["z",1,2]
n3=n1+n2
print(F"combine two list= {n3}")

#11. Remove Empty strings
a1=["ab","","de"," "]
a1.remove(" ")
a1.remove("")
print(a1)

#14.List Comprehension of Numbers
l1=[i for i in range(0,11)]
print(f"list using comprehension= {l1}")

#12. remove Duplicate from list
dup=[1,1,2,2,3,3]
dup2=set(dup)
print(f"after removing the duplicate={dup2}")

#13.Remove all the occurances of specific item from the lsit
occu=[1,1,1,2,3,4]
occu.remove(1)
occu.remove(1)
print(f"removing the occurance of specific item= {occu}")

#15.Access nested list
acc=[[1,2,3],[4,5,6],[7,8,9]]
print(f"access nested list o/p= {acc[0][1]}")
print(f"access nested list o/p= {acc[2][2]}")

#16.flatten nested list
flat_nest=[x for y in acc for x in y]
print(f"flatten nest list={flat_nest}")

#17.concenate two list index wise
conc1=[1,2,3]
conc2=[3,4,5]
conc=conc1[1]+conc2[1]
print(f"adding list index wise={conc}")

#19.Iterate both list
i1=[1,3,5]
i2=[2,4,6]
i3=[(a,b)for (a,b) in zip(i1,i2)]
i4=[x for y in i3 for x in y]
print(f"iterate simulatenously={i4}")

#21. Add new item to list after specified item
q1=[1,2,4,5]
q1.insert(2,3)
print(f"adding new item to list after specified itme= {q1}")

#22.Extend the nested list by adding the sublist
nest=[[1,2],[3,4]]
nest.insert(2, [5,6])
print(f"adding the sublist to nested list={nest}")

#23.replace item
r1=["abc", "xyz"]
r1[1]="def"
print(f"replace item with new item={r1}")


