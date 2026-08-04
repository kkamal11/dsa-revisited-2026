from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        binary_digit = []

        tmp = head
        while tmp:
            val = tmp.val
            binary_digit.append(str(val))
            tmp = tmp.next

        return int("".join(binary_digit), 2)

    def getDecimalValue2(self, head: Optional[ListNode]) -> int:
        ans = 0
        while head:
            ans = ans * 2 + head.val
            head = head.next
        return ans
