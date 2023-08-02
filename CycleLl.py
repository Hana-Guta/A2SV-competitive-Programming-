# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        m = head
        n = head
        while m and m.next:
            n = n.next
            m = m.next.next
            if m == n:
                return True
        return False 
