# soal nomer 1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class StackDoubleLinkedList:
        def __init__(self):
            self.top = None
        
        def is_empty(self):
            return self.top is None
        
        def push(self, item):
            new_node = Node(item)
            if self.top:
                new_node.prev = self.top
            self.top = new_node
            
        def pop(self):
            if self.is_empty():
                print("Stack kosong!")
                return None
            item = self.top.data
            self.top = self.top.prev
            return item
        
        def peek(self):
            if self.is_empty():
                return None
            return self.top.data

stack = StackDoubleLinkedList()
print("Pertama")
stack.push(100)
stack.push(200)
stack.push(300)
print("Pop: ",stack.pop())
print("Pop: ",stack.pop())

print("kedua")
stack.push(50)
stack.push(150)
stack.push(250)
stack.push(350)
print("top stack:", stack.peek())
print("pop: ",stack.pop())

print("=" * 50)
print("=" * 50)

# soal nomer 2.a
class QueueArray:
    def __init__(self, size):
        self.queue = [None] * size
        self.front = 0
        self.rear = -1
        self.size = size
        self.count = 0
        
    def is_empty(self):
        return self.count == 0
    
    def is_full(self):
        return self.count == self.size
    
    def enqueue(self, item):
        if self.is_full():
            print("Queue penuh!")
            return
        self.rear += 1
        self.queue[self.rear] = item
        self.count += 1
        print(f"Setelah nilai {item}: masuk ---> {self.queue}")
        
    def dequeue(self):
        if self.is_empty():
            print("Queue kosong!")
            return None
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front += 1
        self.count -= 1
        print(f"Setelah nilai {item}: masuk ---> {self.queue}")
        return item

queue1 = QueueArray(5)
queue1.enqueue(10)
queue1.enqueue(20)
queue1.enqueue(30)
queue1.enqueue(40)
queue1.enqueue(50)
queue1.dequeue()
queue1.dequeue()
print("Queue setelah skenario 1:", queue1.queue)

queue2 = QueueArray(6)
queue2.enqueue(5)
queue2.enqueue(15)
queue2.enqueue(25)
queue2.enqueue(35)
queue2.enqueue(45)
queue2.enqueue(55)
queue2.dequeue()
queue2.dequeue()
print("Queue setelah skenario 2:", queue2.queue)


print("=" * 50)
print("=" * 50)

# tugas 2.b
class CircularQueue :
    def __init__(self, size):
        self.queue = [None] * size
        self.front = -1
        self.rear = -1
        self.size = size
        
    def is_empty(self):
        return self.front == -1
    
    def is_full(self):
        return (self.rear + 1) % self.size == self.front
    
    def enqueue(self, item):
        if self.is_full():
            print("Queue penuh!")
            return
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item
        print (f"Setelah nilai {item}: masuk ---> {self.queue}")
        
    def dequeue(self):
        if self.is_empty():
            print("Queue kosong!")
            return None
        item = self.queue[self.front]
        self.queue[self.front] = None
        if self.front == self.rear:
                self.front = -1
                self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print(f"Setelah nilai {item}: keluar ---> {self.queue}")
        return item

print("=========== queue ukuran 5 ==========")
cq1 = CircularQueue(5)
print("queue kosong!")
cq1.enqueue(1)
cq1.enqueue(2)
cq1.enqueue(3)
cq1.dequeue()
cq1.enqueue(4)
cq1.enqueue(5)

print("=========== queue ukuran 7 ==========")
cq2 = CircularQueue(7)
cq2.enqueue(10)
cq2.enqueue(20)
cq2.enqueue(30)
cq2.enqueue(40)
cq2.enqueue(50)
cq2.enqueue(60)
cq2.enqueue(70)
print("queue penuh!")
cq2.dequeue()
cq2.dequeue()

print("=" * 50)
print("=" * 50)

# soal nomer 2.c
from collections import deque
class Deque:
    def __init__(self):
        self.deque = deque()

    def add_front(self, item):
        print(f"Sebelum nilai ditambahkan  ---> deque {list(self.deque)}")
        self.deque.appendleft(item)
        print(f"Setelah nilai {item} ditambahkan  --> deque {list(self.deque)}\n")

    def add_rear(self, item):
        print(f"Sebelum nilai ditambahkan  ---> deque {list(self.deque)}")
        self.deque.append(item)
        print(f"Setelah nilai {item} ditambahkan  --> deque{list(self.deque)}\n")

    def remove_front(self):
        print(f"Sebelum nilai ditambahkan  ---> deque {list(self.deque)}")
        item = self.deque.popleft()
        print(f"Setelah nilai {item} dihapus  --> deque {list(self.deque)}\n")
        return item

    def remove_rear(self):
        print(f"Sebelum nilai ditambahkan  ---> deque {list(self.deque)}")
        item = self.deque.pop()
        print(f"Setelah nilai {item} dihapus  --> deque {list(self.deque)}\n")
        return item

print("=========== deque Pertama ==========")
dq1 = Deque()
dq1.add_front(100)
dq1.add_front(200)
dq1.add_front(300)
dq1.add_rear(400)
dq1.add_rear(500)
dq1.remove_front()
dq1.remove_rear()

print("=========== deque Kedua ==========")
dq2 = Deque()
dq2.add_rear(10)
dq2.add_rear(20)
dq2.add_rear(30)
dq2.add_front(40)
dq2.add_front(50)
dq2.remove_front()
dq2.remove_rear()

print("=" * 50)
print("=" * 50)

# soal nomer 2.d
import heapq
class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        print(f"Sebelum nilai masuk   --> {self.queue}")
        heapq.heappush(self.queue, (priority, item))
        print(f"Setelah nilai {item} masuk, menambahkan {priority} prioritas  --> {self.queue}\n")

    def dequeue(self):
        print(f"Sebelum nilai masuk   --> {self.queue}")
        item = heapq.heappop(self.queue)[1]
        print(f"Setelah nilai {item} dihapus --> {self.queue}\n")
        return item
    
print("===============Priority Pertama===============")
pq1 = PriorityQueue()
pq1.enqueue(100, 2)
pq1.enqueue(200, 1)
pq1.enqueue(300, 3)
pq1.dequeue()
pq1.dequeue()

print("===============Priority Kedua===============")
pq1 = PriorityQueue()
pq1.enqueue(10, 5)
pq1.enqueue(30, 3)
pq1.enqueue(20, 4)
pq1.enqueue(50, 2)
pq1.dequeue()

print("=" * 50)
print("=" * 50)

# soal nomer 2.e
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        print("\nSebelum nilai ditambahkan  --> ", end="")
        self.display()
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"Setelah nilai {item} ditambahkan  --> ", end="")
        self.display()

    def dequeue(self):
        print("\nSebelum nilai dihapus  --> ", end="")
        self.display()
        if self.is_empty():
            print("Queue kosong!")
            return
        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        print(f"Setelah nilai {item} dihapus  --> ", end="")
        self.display()

    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("None")

print("===============Queue dengan linked List pertama===============")
ql1 = QueueLinkedList()
ql1.enqueue(8)
ql1.enqueue(16)
ql1.enqueue(24)
ql1.dequeue()
ql1.enqueue(32)
ql1.enqueue(40)
ql1.dequeue()

print("===============Queue dengan linked List kedua===============")
ql2 = QueueLinkedList()
ql2.dequeue()
ql2.enqueue(11)
ql2.enqueue(22)
ql2.enqueue(33)
ql2.dequeue()
ql2.enqueue(44)
ql2.enqueue(55)
ql2.dequeue()
print("=" * 50)
print("=" * 50)
