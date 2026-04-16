# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        if not head1:
            return head2
        if not head2:
            return head1
        head = None
        prev = None
        while head1 and head2:
            if head1.val <= head2.val:
                if head == None:
                    head = head1
                    prev = head1
                else:
                    prev.next = head1
                prev = head1
                head1 = head1.next
            else:
                if head == None:
                    head = head2
                    prev = head2
                else:
                    prev.next = head2
                prev = head2
                head2 = head2.next
        if not prev:
            return head
        elif head1:
            prev.next = head1
        elif head2:
            prev.next = head2
        return head


        