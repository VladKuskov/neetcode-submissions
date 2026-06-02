# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen_node = set()
        # traverse listA, add each obj to set
        while headA:
            seen_node.add(headA)
            headA = headA.next
        # check if node object exists in set,
        # if yes, return the intersection/obj
        while headB:
            if headB in seen_node:
                return headB
            else:
                headB = headB.next