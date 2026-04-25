# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num = 0

        count = 1
        while l1:
            num = num + (l1.val)*count
            count *= 10
            l1 = l1.next
        
        count = 1
        while l2:
            num = num + (l2.val)*count
            count *= 10
            l2 = l2.next

        if num == 0:
            return ListNode(0)
            
        head = None
        p = None
        while num:
            digit = num % 10
            print(num, digit)
            if head == None:
                head = ListNode(digit)
                p = head
            else:
                p.next = ListNode(digit)
                p = p.next
            num = num // 10
        return head

