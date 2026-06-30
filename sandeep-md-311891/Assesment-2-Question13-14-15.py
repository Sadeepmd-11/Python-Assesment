employees = [
    {"name": "A", "salary": 50}, 
    {"name": "B", "salary": 70}, 
    {"name": "C", "salary": 60}
]

employees.sort(key=lambda x:x["salary"], reverse=True)
print(employees)

#------------------------------------------------------
#Question 14

list1=list(map(int, input("enter a set1:").split()))
list2=list(map(int, input("enter a set2:").split()))

set1=set(list1)
set2=set(list2)

if set1.issubset(set2):
    print(" Set1 is a subset of set2")
elif set1.issuperset(set2):
    print(" Set1 is a superset of set2")
elif set1.isdisjoint(set2):
    print(" Set1 is a disjoint of set2")
else:
    print("set1 and set2 are overlapping")

#--------------------------------------------------
#Question 15
list1 = [101, 102, 103]
list2=[103,104,105]
list3= list1 + list2
print(set(list3))

