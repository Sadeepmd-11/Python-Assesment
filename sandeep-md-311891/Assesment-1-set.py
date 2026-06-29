#1.Basic set operations

# Create two sets
set1 = {1, 2, 3, 4}
set2 = {1, 2, 5, 6}
print(f"set1={set1}")
print(f"set2={set2}")

#adding elemet to set
set1.add(6)
print(set1)

#remove the element from the set
set1.remove(6)
print(set1)

#2.uninon of the set
print(f"union of the set={set1 | set2}")

#3.intersection of the set
print(f"intersection of the set={set1 & set2}")

#4.difference of the set
print(f" differnce of the set={set1-set2}")

#5.symmetric differnce
print(f"symmetric differnce of set={set1^set2}")

#6.add list of element to set

list1 = [4, 5, 6]
set1.update(list1)

print(f"add list of element to set={set1}")

#7.differnce update of set
set1.difference_update(set2)

print(set1)

#8.remove items from set simulatenously
set4 = {1,2,3,4,5,6,7}

remove_items = {3,5,7}

set4.difference_update(remove_items)

print(set4)

#9.check subset
print(f"check subset ={set1 <= set2}")

#10.check superset
print(f"check superset ={set1 >= set2}")

#11. set intersection
print(f"intersection of the set={(len(set1 & set2)>0)}")

#12.symmetric_difference_update
set1.symmetric_difference_update(set2)
print(set1)

#13.intersection update
set1.intersection_update(set2)
print(set1)

#14.commom elementsin two list
l1=[1,2,3,4]
l2=[2,4,5,6]
common=list(set(l1) & set(l2))
print(common)

#15.frozen set
f = frozenset([1, 2, 3, 4])
print(f"frozen set={f}")

#16.count unique words
text = "abc xyz abc ide xyz"

w = text.split()

unique = len(set(w))

print(unique)