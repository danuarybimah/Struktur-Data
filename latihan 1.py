class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 
        self.prev = None

class DoubleLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail 
            self.tail.next = new_node  
            self.tail = new_node  
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:  
            self.head = None
            self.tail = None
        else:
            self.tail = temp.prev 
            self.tail.next = None 
            temp.prev = None 
        self.length -= 1
        return temp.value

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head 
            self.head.prev = new_node 
            self.head = new_node   
        self.length += 1

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.prepend(value)
            return True
        if index == self.length:
            self.append(value)
            return True
        new_node = Node(value)
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        new_node.next = temp.next 
        new_node.prev = temp
        if temp.next: 
            temp.next.prev = new_node
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            removed_node = self.head
            self.head = self.head.next
            if self.head: 
                self.head.prev = None
            self.length -= 1
            return removed_node.value
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        removed_node = temp.next
        temp.next = removed_node.next
        if removed_node.next: 
            removed_node.next.prev = temp
        self.length -= 1
        return removed_node.value
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
        print("None")

my_list = DoubleLinkedList(10)
my_list.append(20)
my_list.insert(1, 15)
my_list.remove(1)
my_list.print_list()