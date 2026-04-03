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


sol = Solution()
s = "(1+(2*3)+((8)/4))+1"
s2 = "()(())((()()))"
print(sol.maxDepth(s))
print(sol.maxDepth(s2))
