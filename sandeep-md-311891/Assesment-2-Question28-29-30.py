import time 
def timer(func):
    def wrapper():
        start=time.time()
        func()
        end=time.time()
        print(f"function {func.__name__} took {end - start:.4f} seconds to run")
    return wrapper

@timer
def waste_time():
    time.sleep(1.5)

waste_time()

#------------------------------------------------------------

#Question29
def fibonacci(n):
    a,b=0,1

    for i in range(n):
        yield a
        a,b=b,a+b

n=8
print(f"First {n} fibanocci numbers are:")
for x in fibonacci(n):
    print(x, end=" ")