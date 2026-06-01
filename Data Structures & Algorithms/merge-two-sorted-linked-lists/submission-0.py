# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        dummy = ListNode(0)
        current = dummy
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                # add the smallest of the two to current.next, for l1
                current.next = l1
                current = current.next
                l1 = l1.next
            else:
                # add the smallest of the two to current.next, for l2
                current.next = l2
                current = current.next
                l2 = l2.next

        if l1 is not None:
            current.next = l1
        if l2 is not None:
            current.next = l2
        return dummy.next        