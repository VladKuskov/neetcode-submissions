# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        # save head in current to not mess with head
        current = head
        while current:
            current = current.next
            length += 1
        position = length - n
        # this lands at the first node, so just skip the head node.
        if position == 0:
            return head.next
        # moved current when counting the length, this resets it to head
        current = head
        # get to the node BEFORE the one that needs to be "removed"
        # remove it by setting current.next to current.next.next.
        for i in range(position - 1):
            current = current.next
        current.next = current.next.next
        return head