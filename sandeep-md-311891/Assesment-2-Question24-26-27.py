class Queue:
    def __init__(self):
        self.queue=[]
    
    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue)==0:
            return "queue is empty"
        return self.queue.pop(0)
    
    def peek(self):
        return self.queue[0]
    
q=Queue()
q.enqueue("Customer A")
q.enqueue("Customer B")

print("Serving:", q.dequeue())
print("Next in line:", q.peek())

#---------------------------------------------------
#Question26

employees = [
    ("Alice", 30, 50000),
    ("Bob", 25, 75000),
    ("Charlie", 35, 60000)
]


result = sorted(employees, key=lambda x: x[2], reverse=True)

print(result)

#-------------------------------------------------
#question27
nums=[1,2,3,4,5,6]
res=list(map(lambda x: x**2, filter(lambda x: x%2==0, nums)))
print(res)