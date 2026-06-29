#Basic Tuple operations

#Creating and printing the Tuple
t1=("name","age","place","state")
print(t1)

#accessing the element
print(f"accessing the elements= {t1[0]}")

#length of the tuple
print(f"legth of tuple= {len(t1)}")

#2.tuple repetition
t2=t1 *3
print(f"tuple repetiotn={t2}")

#3.slicing tuples
t3=t1[0::2]
print(f"slicing the tuple={t3}")

#4.reverse the tuple
t4=tuple(reversed(t1))
print(t4)

#5.Access nested tuples
a1=("biodata",("name", "age"))
print(f"accesing nested tuples={a1[1][1]}")

#6.create a tuple with single item 50
s1=(50,)
print(type(s1))

#7.unpack the tuple 
u1=("ab",1,"a",2)
a,b,c,d=u1
print(f"unpaked the element={a}")
print(f"unpaked the element={b}")
print(f"unpaked the element={c}")
print(f"unpaked the element={d}")

#8.swap the tuple
sw1=(1,2,3)
sw2=(4,5,6)
sw1,sw2=sw2,sw1
print(f"After swapping the tuple={sw1}")
print(f"After swapping the tuple={sw2}")

#9.copy specific elemet from tuple
c1= (1,2,3,4,5,6,7)
c2=c1[1:4]
print(f"copy specific elemnt={c2}")

#10. list to tuple
list1 = [11,1,1,2,3,44]
tuple2=tuple(list1)
print(f"list to tuple={tuple2}")

#11.fuction returning tuple

def calculation(a,b):
    add = a + b
    sub = a - b
    return add, sub

result = calculation(40, 10)
print(f" result of function returning tuple={result}")

#12.compare the tuple
tuple4 = (10, 20, 30)
tuple5 = (1,2,3)

print(tuple4 < tuple5)
print(tuple4 > tuple5)

#13.remove duplicates
r1=tuple(set(tuple2))
print(f"removing the duplicates={r1}")

#14.filter the elements
num=(2,4,1,6,7,8)
odd_no=tuple(x for x in num if x%2==0)
print(odd_no)

#15.mapping the elements
fruits = ("apple", "banana", "mango")

result = tuple(map(str.upper, fruits))

print(f"mapping the element={result}")

#16.modify the tuple
list_tuple4=list(tuple4)
list_tuple4[2]=12
mod_tup=tuple(list_tuple4)
print(mod_tup)

#17.sorting a tuple by second element
d1 = ((1, 9), (3, 18), (9, 2), (4, 5))

sorted_d1 = tuple(sorted(d1, key=lambda x: x[1]))

print(f"sorted_d1={sorted_d1}")


#18. count a elemetn in tuple
cou=tuple2.count(1)
print(f"count of 1 is {cou}")

#19.check all elements in tuples are same
c1 = (2,2,2,2)

result = all(x == c1[0] for x in c1)

print(result)