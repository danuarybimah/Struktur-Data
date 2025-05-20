class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 
        self.prev = None

class DoubleLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def display(self) :
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
        print("None")

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp 
            temp = temp.next
        pre.next = None
        self.tail = pre
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
    
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail =new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
 
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.head
        for _ in range (index - 1 ):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            removed_node = self.head
            self.head = self.head.next
            self.length -=1
            return removed_node.value
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        removed_node = temp.next
        temp.next = removed_node.next
        self.length -=1 
        return removed_node.value
    
my_list = DoubleLinkedList(10)
my_list.append(20)
my_list.insert(2, 15)
my_list.remove(1)
my_list.display()