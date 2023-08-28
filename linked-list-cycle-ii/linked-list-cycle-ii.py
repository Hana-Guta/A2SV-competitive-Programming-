# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def has_cycle(head):
            slow = head
            fast = head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

                if slow == fast:
                    return True

            return False

        def find_meeting_point(head):
            slow = head
            fast = head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

                if slow == fast:
                    return slow

            return None

        if not head or not head.next:
            return None

        meeting_point = find_meeting_point(head)

        if not meeting_point:
            return None

        ptr1 = head
        ptr2 = meeting_point

        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1
