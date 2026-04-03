class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in (s + s)


s = "abcde"
goal = "cdeab"
sol = Solution()
print(sol.rotateString(s, goal))
