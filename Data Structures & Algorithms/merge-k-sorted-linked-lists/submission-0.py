# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = None
        p = None
        k = len(lists)
        while any(lists):
            min_ele = 1111
            top_k = -1
            top_node = None
            for i in range(k):
                if lists[i] and lists[i].val < min_ele:
                    min_ele = lists[i].val
                    top_node = lists[i]
                    top_k = i            

            lists[top_k] = lists[top_k].next
            if not head:
                head = top_node
                p = top_node
            else:
                p.next = top_node
                p = p.next
        return head
                


        