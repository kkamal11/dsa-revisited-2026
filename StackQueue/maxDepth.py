class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        curr_depth = 0
        for char in s:
            if char == "(":
                curr_depth += 1
                max_depth = max(curr_depth, max_depth)
            elif char == ")":
                curr_depth -= 1
        return max_depth

    def maxDepth2(self, s: str) -> int:
        stack = []
        max_depth = 0
        for ch in s:
            if ch == "(":
                stack.append("(")
                max_depth = max(max_depth, len(stack))
            elif ch == ")" and stack:
                stack.pop()
        
        return max_depth
