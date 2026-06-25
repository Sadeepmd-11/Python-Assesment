#1.Perform basic dictionary operations

#Print the dictionary
n1={"name":"xyz", "age":12, "place":"bengaluru"}
print(n1)

#add the new item to the dict
n1["state"]="Karnataka"
print(f"added new item to list={n1}")

#accesing the element in dict
print(f"accesing the element={n1["name"]}")

#update the value
n1["age"]=10
print(f"updating the value={n1}")

#2.Perform dictionary operations
#deleting the key
n1.pop("state")
print(f"deleting using pop={n1}")
n1["state"]="karnatka"
del n1["state"]
print("deleting the key using del ={n1}")

#Get all keys
print(f"prints key={n1.keys()}")

#get all values
print(f"print all the values={n1.values()}")

#get all key-values in pairs
print(f"print all the values={n1.items()}")

#3.Dict from list
d1=[1,2,3]
d2=["one","two","three"]
d3=dict(zip(d1,d2))
print(f"dict from list={d3}")

#4.clear a dict
n1.clear()
print(n1)

#5.merge two dict into one
di1={"name":"xyz", "age":12, "place":"bengaluru"}
di2={1: 'one', 2: 'two', 3: 'three'}
di1.update(di2)
print(di1)

#6.count character frequencies
a="aabbccccd"
frequency={}
for ch in a:
    if ch in frequency:
        frequency[ch]+=1
    else:
        frequency[ch]=1
print(f"frequency of character={frequency}")

#7.access nested dict
acc_di1={
    "biodata": {
        "name":"xyz",
        "age":12,
        "history":"not sure"
    }
}
print(f"accesing nested dict={acc_di1["biodata"]["age"]}")

#8.accesing specific keywork history from nested dict
print(f"accesing history key={acc_di1["biodata"]["history"]}")

#9.Modify nested dict
acc_di1["biodata"]["name"]="def"
print(acc_di1)

#10.Initialize dict with default values
keey=[1,2,3]
k={x: 0 for x in keey}
print(k)

#11.create a dict by extracting keys from given dict
c1={"name":"xyz", "age":12, "place":"bengaluru"}
c2={x: 0 for x in c1}
print(f"dict by extracting keys from given dict={c2}")

#12.Delete a list of keys from a dictionary
c1={"name":"xyz", "age":12, "place":"bengaluru"}
key_delete=["age", "place"]
c2={k: v for k,v in c1.items() if k not in key_delete}
print(f"Delete a list of keys from a dictionary={c2}")

#13.check if value exist in dict
if 12 in c1.values():
    print("found")
else:
    print("not found")

#14.rename key of dict
c1["full name"]=c1.pop("name")
print(f"rename={c1}")

#15.key of minimum value
e1={"name":11, "age":12, "place":9}
minimum=min(e1, key=e1.get)
print(f"minimum value in dict: {minimum}, {e1[minimum]}")

#16.chnage the value of key in nested dit
acc_di1={
    "biodata": {
        "name":"xyz",
        "age":12,
        "history":"not sure"
    }
}
acc_di1["biodata"]["age"]=14
print(f"change the value of key in nested= {acc_di1}")

#17.#invert a dicti
e1={"name":11, "age":12, "place":9}
inverted={val: key for key, val in e1.items()}
print(f"invert a dicti= {inverted}")

#18.sort dict by keys
sort_keys=dict(sorted(e1.items()))
print(f"sorted keys={sort_keys}")

#19.sort dict by values
sort_val=dict(sorted(e1.items(), key=lambda x:x[1]))
print(f"sorted valyes={sort_val}")

#20.check if all values are unique
if len(e1.values())==len(set(e1.values())):
    print("all are unique")
else:
    print("not unique")