# definition of linked-list
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head

        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next

        new_head_index = (length - k % length) % length

        if new_head_index == 0:
            return head

        current = head
        for _ in range(new_head_index - 1):
            current = current.next

        new_head = current.next
        current.next = None
        tail.next = head

        return new_head

