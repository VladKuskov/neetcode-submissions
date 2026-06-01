# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        while current is not None:
            # [0, 1, 2, 3]
            # next_ node = node 1
            next_node = current.next
            # 0.next = None
            current.next = prev
            # prev = node 0
            prev = current
            # current = node 1
            # when on the last step of 0->1->2->3, next_node is None for 3, and current = None. so stop.
            current = next_node

        return prev