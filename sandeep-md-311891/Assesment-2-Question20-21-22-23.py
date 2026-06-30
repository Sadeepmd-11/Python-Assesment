#Question-20

class PowerOfTwo:
    def __init__(self, max_exp):
        self.max_exp=max_exp
        self.current_exp=0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current_exp > self.max_exp:
            raise StopIteration
        
        value = 2 ** self.current_exp
        self.current_exp+=1
        return value
        
power1= PowerOfTwo(3)
for p in power1:
    print(p, end=" ")

#-----------------------------------------------------

#Question21
def dup_elements(number):
    seen=set()
    dup=set()

    for i in number:
        if i in seen:
            dup.add(i)
        else:
            seen.add(i)
    return dup

number=[1, 2, 3, 2, 4, 5, 1, 6]
print(f"{dup_elements(number)}")

#----------------------------------------------
#Question 22
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    
    def append(self,data):
        new_node=Node(data)

        if self.head is None:
            self.head=new_node
            return
        
        current=self.head
        while current.next:
            current=current.next

        current.next=new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)

ll.display()

#----------------------------------------
#Question23

