# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def get_node_value(self, node):
        return node.val if node else None

    def __str__(self):
        return str(self.val) + " -> " + str(self.next)


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode(-1)
        stack = []
        tmp = head
        curr = dummy

        while tmp:
            stack.append(tmp.val)

            if len(stack) == 2:
                while stack:
                    node = ListNode(stack.pop())
                    curr.next = node
                    curr = node

            tmp = tmp.next

        if stack:
            curr.next = ListNode(stack.pop())

        return dummy.next
