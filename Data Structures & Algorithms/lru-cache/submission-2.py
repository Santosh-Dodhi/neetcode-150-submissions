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
            return self.add(key, value)
            
        if node and node.prev == None and node.next:
            tmp = self.head
            self.head = self.head.next
            self.head.prev = None
            del tmp
            return self.add(key, value)
    
    def print_dll(self):
        node = self.head
        while node:
            print((node.key, node.value), end=" ")
            node = node.next


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

        # print()
        # node = self.queue.head
        # while node:
        #     if node.key == key:
        #         self.queue.remove_and_add(key, node.value)
        #         self.queue.print_dll()
        #         return node.value
        #     node = node.next
        # return -1
        

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




        # print()
        # node = self.queue.head
        # while node:
        #     if node.key == key:
        #         node.value = value
        #         self.queue.remove_and_add(key, value)
        #         self.queue.print_dll()
        #         return
        #     node = node.next
    
        # if self.n > 0:
        #     self.queue.add(key, value)
        #     self.n -= 1
        #     self.queue.print_dll()
        #     return
        # else:
        #     self.queue.remove_and_add(self.queue.head.key, self.queue.head.value)
        #     self.queue.print_dll()
        #     self.queue.tail.key = key
        #     self.queue.tail.value = value
        #     self.queue.print_dll()
        #     return

        
