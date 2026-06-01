# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # solution with a set. There is a cycle if head is in seen_nodes, so return True.
        seen_nodes = set()
        while head is not None:
            if head not in seen_nodes:
                seen_nodes.add(head)
            else:
                return True
            head = head.next
        return False