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

    def addTwoNumbersOptimized(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        result = ListNode()
        temp = result
        carry = 0
        while l1 or l2 or carry:
            sum_ = 0
            if l1:
                sum_ += l1.val
                l1 = l1.next
            if l2:
                sum_ += l2.val
                l2 = l2.next

            if carry:
                sum_ += carry

            addition = sum_ % 10
            carry = sum_ // 10
            temp.next = ListNode(addition)
            temp = temp.next
        return result.next
