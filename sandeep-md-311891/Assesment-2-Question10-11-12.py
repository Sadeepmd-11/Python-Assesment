def rotate_list(list,n,direction):
    
    if direction == "right":
        return list[-n:] + list[:-n]
    elif direction == "left":
        return list[n:] + list[:n]
    else:
        print("invalid direction")

list=[1, 2, 3, 4, 5]
n=2
direction="left"

print(rotate_list(list, n, direction))

#--------------------------------------------------
#Question 11
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

d3={}
for key,value in d1.items():
    d3[key]=[value]

for key,value in d2.items():
    if key in d3:
        d3[key].append(value)
    else:
        d3[key]=[value]

print(d3)

#-------------------------------------------------------
#Question 12
def inverts(dict):
    inverted={}

    for key, values in dict.items():
        for book in values:
            inverted[book]=key
    
    return inverted

dict= {
    "Orwell": ["1984", "Animal Farm"],
    "Huxley": ["Brave New World"]
}
print(inverts(dict))

    
    