def logger(message,*args, **kwargs):
    print(f"Event: {message}")
    print(f"details: {args}")
    print(f"metadata: {kwargs}")

logger("User Login", "admin", "dashboard", timestamp="10:00 AM", status="Success")


#-----------------------------------------------
#Question 32
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

dict=dict(zip(names, scores))

sort=sorted(dict.items(), key=lambda x:x[1], reverse=True)

for rank, (names,scores) in enumerate(sort, start=1):
    print(f"Rank {rank}: {names} scored {scores}")

#------------------------------------------------
#Question34
trial = [1, 2, 3, 4, 5]
paid = [4, 5, 6, 7, 8]

trail_set=set(trial)
paid_set=set(paid)


Both= trail_set & paid_set
Trial_only=trail_set - paid_set
not_both=trail_set ^ paid_set

print(f"upgraded: {Both}")
print(f"Leads: {Trial_only}")
print(f"unique status: {not_both}")
