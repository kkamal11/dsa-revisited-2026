class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        count = 0

        for ch in s:
            if ch == ")":
                if not stack:
                    return False
                
                last = stack.pop()
                if not (last != "(" or last != "*"):
                    return False
            elif ch == "*":
                pass
            else:
                stack.append(ch)
            print(stack)
                
        return stack == []

sol = Solution()
s = "(((*))"
print(sol.checkValidString(s))