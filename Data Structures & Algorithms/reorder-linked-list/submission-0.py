# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # get the mid location
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow

        #reverse the second half
        p = None
        q = mid
        r = mid.next if mid else None
        while q:
            q.next = p
            p = q
            q = r
            r = r.next if r else None
        head2 = p
        
        # lets join the 1st half & reversed second half
        p = head
        q = p.next if p else None
        r = head2
        s = head2.next if head2 else None

        while q:
            p.next = r
            if r:
                r.next = q
            p = q
            q = q.next if q else None
            r = s
            s = s.next if s else None


        
        