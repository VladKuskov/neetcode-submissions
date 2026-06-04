"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # empty list case
        if not head:
            return None
        copy = head
        copy_dict = {}
        # map original node to copies
        while copy:
            copy_dict[copy] = Node(copy.val)
            copy = copy.next

        # traverse again, wiring .next and .random for each node.
        # new node's .next should point to the COPY of original.next, so:
        #
        copy = head
        while copy:
            # the new node value in dict = copy.next (original) if it
            # exists in the dict.
            copy_dict[copy].next = copy_dict.get(copy.next)
            copy_dict[copy].random = copy_dict.get(copy.random)
            copy = copy.next

        return copy_dict[head]