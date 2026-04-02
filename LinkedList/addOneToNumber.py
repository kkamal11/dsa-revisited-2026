class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        L = []
        tmp = self
        while tmp:
            L.append(tmp.val)
            tmp = tmp.next
        return "".join(str(n) for n in L)


class Solution:
    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def addOne(self, head):
        head = self.reverse(head)
        curr = head
        carry = 1
        while curr and carry:
            curr.val += carry
            if curr.val < 10:
                carry = 0
            else:
                curr.val = 0
                carry = 1
            prev = curr
            curr = curr.next
        if carry:
            prev.next = ListNode(1)
        return self.reverse(head)

    def add1ToNumber(self, head: ListNode):
        if head is None:
            return 0
        if head.next is None:
            sum_ = head.val + 1
            head = ListNode(sum_)
            return head
        num = 0
        tmp = head
        while tmp:
            num = num * 10 + int(tmp.val)
            tmp = tmp.next
        num = num + 1
        div = 1
        temp_num = num
        while temp_num >= 10:
            div *= 10
            temp_num //= 10
        res = None
        while num > 0:
            d = num // div
            if res is None:
                res = ListNode(d)
                curr = res
            else:
                curr.next = ListNode(d)
                curr = curr.next
            num = num % div
            div = div // 10
        return res


first = ListNode(4)
second = ListNode(5)
third = ListNode(6)
first.next = second
second.next = third
head = first
print(head)
sol = Solution()
print(sol.add1ToNumber(head))
print(sol.addOne(head=head))
