class Solution:
    def reverseParentheses(self, s: str) -> str:
        """
        (ed(et(oc))el)
        (ed(etco)el)
        (edocteel)
        leetcode

        (ed(et(oc
        (ed(etco


        Complexity Analysis
        Time complexity : O(n). We traverse the input string once.
        Space complexity : O(n). We use a stack to store the characters of the input string.
        """
        stack = []
        inner = []
        for ch in s:
            if ch == ")":
                while stack:
                    last = stack.pop()
                    if last == "(":
                        stack.extend(inner)
                        inner = []
                        break
                    inner.append(last)
            else:
                stack.append(ch)

        return "".join(stack)

    def reverseParentheses2(self, s: str) -> str:
        stack = []
        inner = []
        for ch in s:
            if ch == ")":
                while stack:
                    last = stack.pop()
                    if last == "(":
                        stack.extend(inner)
                        inner = []
                        break
                    inner.append(last)
            else:
                stack.append(ch)

        return "".join(stack)
