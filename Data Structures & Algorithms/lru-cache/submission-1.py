class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class DoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add(self, key, value):
        if self.head == None and self.tail == None:
            self.head = Node(key, value)
            self.tail = self.head 
        else:
            self.tail.next = Node(key, value)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
    
    def remove_and_add(self, key, value):
        node = self.head
        while node:
            if node.key == key:
                break
            else:
                node = node.next
        if node and node.prev != None and node.next != None:
            node.prev.next = node.next
            node.next.prev = node.prev
            del node
            self.add(key, value)
            return
        
        if node and node.prev == None and node.next:
            tmp = self.head
            self.head = self.head.next
            self.head.prev = None
            del tmp
            self.add(key, value) 
            return
    
    def print_dll(self):
        node = self.head
        while node:
            print((node.key, node.value), end=" ")
            node = node.next




class LRUCache:

    def __init__(self, capacity: int):
        self.n = capacity
        self.queue = DoublyLL()
        
    def get(self, key: int) -> int:
        print()
        node = self.queue.head
        while node:
            if node.key == key:
                self.queue.remove_and_add(key, node.value)
                self.queue.print_dll()
                return node.value
            node = node.next
        return -1
        

    def put(self, key: int, value: int) -> None:
        print()
        node = self.queue.head
        while node:
            if node.key == key:
                node.value = value
                self.queue.remove_and_add(key, value)
                self.queue.print_dll()
                return
            node = node.next
    
        if self.n > 0:
            self.queue.add(key, value)
            self.n -= 1
            self.queue.print_dll()
            return
        else:
            self.queue.remove_and_add(self.queue.head.key, self.queue.head.value)
            self.queue.print_dll()
            self.queue.tail.key = key
            self.queue.tail.value = value
            self.queue.print_dll()
            return

        
