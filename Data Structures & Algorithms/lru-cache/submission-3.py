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
    
    def append(self, key, value):
        if self.head == None and self.tail == None:
            self.head = Node(key, value)
            self.tail = self.head 
        else:
            self.tail.next = Node(key, value)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next

        return self.tail
    
    def remove(self, node):
        # middle ele
        if node and node.prev and node.next:
            node.prev.next = node.next
            node.next.prev = node.prev
            del node
            return

        
        # front ele
        if node and node.next:
            tmp = self.head
            self.head = self.head.next
            self.head.prev = None
            del tmp
            return
        
        # end node
        if node and node.prev:
            tmp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            del tmp
            return 
        
        # only one ele
        if node:
            self.head = None
            self.tail = None
            del node
            return
    
    # def print_dll(self):
    #     node = self.head
    #     while node:
    #         print((node.key, node.value), end=" ")
    #         node = node.next


class LRUCache:
    def __init__(self, capacity: int):
        self.n = capacity
        self.queue = DoublyLL()
        self.mapp = dict()
        
    def get(self, key: int) -> int:
        if key in self.mapp:
            self.queue.remove(self.mapp[key])
            self.mapp[key] = self.queue.append(key, self.mapp[key].value)
            return self.mapp[key].value
        return -1        

    def put(self, key: int, value: int) -> None:
        if key in self.mapp:
            self.queue.remove(self.mapp[key])
            self.mapp[key] = self.queue.append(key, self.mapp[key].value)
            self.mapp[key].value = value
            return
        elif self.n > 0:
            self.mapp[key] = self.queue.append(key, value)
            self.n -= 1
            return
        else:
            node = self.queue.head
            del self.mapp[node.key]
            self.queue.remove(node)
            self.mapp[key] = self.queue.append(key, value)
            return

        
