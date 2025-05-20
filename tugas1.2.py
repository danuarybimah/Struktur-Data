class Node:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, nim, nama):
        new_node = Node(nim, nama)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def pop(self):
        if not self.tail:
            return None
        popped_node = self.tail
        if self.tail.prev:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.head = None
            self.tail = None
        return popped_node

    def prepend(self, nim, nama):
        new_node = Node(nim, nama)
        if not self.head: 
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert(self, index, nim, nama):
        if index == 0:
            self.prepend(nim, nama)
            return
        new_node = Node(nim, nama)
        current = self.head
        for _ in range(index - 1):
            if current is None:
                raise IndexError("Index out of bounds")
            current = current.next
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        if new_node.next is None:
            self.tail = new_node

    def remove(self, nim):
        current = self.head
        while current:
            if current.nim == nim:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head: 
                    self.head = current.next
                if current == self.tail: 
                    self.tail = current.prev
                return current
            current = current.next
        return None 

    def print_list(self):
        current = self.head
        while current:
            print(f"NIM: {current.nim}, Nama: {current.nama}")
            current = current.next

# Contoh penggunaan
dll = DoubleLinkedList()
dll.append("123", "Bima")
dll.append("456", "Andre")
dll.prepend("789", "Dava")
dll.insert(1, "101", "Alvin")
print("\nList setelah append, prepend, dan insert:")
dll.print_list()
print("\nList setelah pop:")
dll.print_list()
print("\nList setelah Remove:")
dll.remove("456")
dll.print_list()