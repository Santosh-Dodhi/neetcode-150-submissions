# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get total no. of nodes
        count = 0
        p = head
        while p:
            count += 1
            p = p.next
        
        target = count - n
        if target == 0:
            head = head.next
            return head

        q = head
        while target-1 > 0:
            q = q.next
            target -= 1

        q.next = q.next.next if q.next else None
        return head
            


            
