# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        result = None
        curr = None
        a = l1
        b = l2
        prev_carry = carry = 0
        while a and b:
            aval = a.val
            bval = b.val
            add = aval + bval + prev_carry
            if add >= 10:
                carry = add // 10
                add = add % 10
            else:
                carry = 0
            if result is None:
                result = ListNode(add)
                curr = result
            else:
                curr.next = ListNode(add)
                curr = curr.next
            prev_carry = carry
            a = a.next
            b = b.next

        while a:
            aval = a.val
            add = aval + prev_carry
            if add >= 10:
                carry = add // 10
                add = add % 10
            else:
                carry = 0
            if result is None:
                result = ListNode(add)
                curr = result
            else:
                curr.next = ListNode(add)
                curr = curr.next
            prev_carry = carry
            a = a.next

        while b:
            aval = b.val
            add = aval + prev_carry
            if add >= 10:
                carry = add // 10
                add = add % 10
            else:
                carry = 0
            if result is None:
                result = ListNode(add)
                curr = result
            else:
                curr.next = ListNode(add)
                curr = curr.next
            prev_carry = carry
            b = b.next
        if prev_carry > 0:
            node = ListNode(prev_carry)
            curr.next = node
        return result
