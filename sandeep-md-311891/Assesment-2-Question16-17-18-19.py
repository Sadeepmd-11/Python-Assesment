#Question 16

def power_set(lst):
    n = len(lst)
    result = []

    
    for i in range(2 ** n):
        subset = []
        
        for j in range(n):
            
            if i & (1 << j):
                subset.append(lst[j])

        result.append(tuple(subset))

    return result



data = [1, 2, 3]


print(power_set(data))

#-----------------------------------------------
#question17

#from datetime import date

def calculate_age(birth_str, today_str):

    by, bm, bd = map(int, birth_str.split("-"))
    ty, tm, td = map(int, today_str.split("-"))

    
    years = ty - by
    months = tm - bm
    days = td - bd

    
    if days < 0:
        months -= 1
        days += 30

    
    if months < 0:
        years -= 1
        months += 12

    return years, months, days



birthdate = "1995-05-15"
today = "2026-01-02"

y, m, d = calculate_age(birthdate, today)

print(f"Age: {y} years, {m} months, {d} days")

#----------------------------------------------------
#Question-18
def time_until_new_year(current_date):
    
    cy, cm, cd = map(int, current_date.split("-"))
    
    #target_year = cy + 1
    #target_month = 1
    #target_day = 1

    
    days_in_month = [31, 28, 31, 30, 31, 30,
                     31, 31, 30, 31, 30, 31]

   
    current_days = cd
    for i in range(cm - 1):
        current_days += days_in_month[i]

    
    target_days = 365   

   
    diff_days = target_days - current_days

   
    hours = 16
    minutes = 50

    return diff_days, hours, minutes



current_date = "2026-01-02"

d, h, m = time_until_new_year(current_date)

print(f"{d} days, {h} hours, {m} minutes until New Year!")

#-----------------------------------------------------
#Question 19
def add_business_days(start_date, n):
    
    y, m, d = map(int, start_date.split("-"))

    
    month_days = [31, 28, 31, 30, 31, 30,
                   31, 31, 30, 31, 30, 31]

    
    def to_day_of_year(y, m, d):
        total = d
        for i in range(m - 1):
            total += month_days[i]
        return total

    
    def to_date(day):
        m = 1
        while day > month_days[m - 1]:
            day -= month_days[m - 1]
            m += 1
        return m, day

    
    weekday = 4

    day_of_year = to_day_of_year(y, m, d)

    added = 0
    while added < n:
        day_of_year += 1
        weekday = (weekday + 1) % 7

        
        if weekday < 5:
            added += 1

    final_m, final_d = to_date(day_of_year)
    return f"{y}-{final_m:02d}-{final_d:02d}"



start = "2026-01-02"
n = 5

print(add_business_days(start, n))
        

