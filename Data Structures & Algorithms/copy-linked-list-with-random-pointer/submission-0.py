"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        p = head
        q = None # head2
        count = 0
        # create copy without random
        while p:
            count += 1
            if q == None:
                q = Node(p.val)
                head2 = q
            else:
                q.next = Node(p.val)
                q = q.next
            p = p.next
        
        # copy the random pointer
        p = head
        q = head2
        while p:
            target = p.random
            tmp_cnt = 0
            while target:
                tmp_cnt += 1
                target = target.next
            
            # go till n - tmp_cnt in q
            r = None
            tmp_chk = count - tmp_cnt
            while tmp_chk:
                if not r: 
                    r = head2
                else:
                    r = r.next
                tmp_chk -= 1
            q.random = r.next if r else head2
            q = q.next
            p = p.next
        
        return head2




