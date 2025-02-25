class Node:
    def _init_(self, value):
        self.value = value
        self.next = "none" 

class LinkedList:
    def _init_(self,value):
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