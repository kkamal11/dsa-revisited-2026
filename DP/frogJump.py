class Solution:
    def frogJumps(self, heights):
        n = len(heights)
        dp = [0] * n
        for i in range(1,n):
            one = dp[i-1] + abs(heights[i] - heights[i-1])

            two = float('inf') if i == 1 else dp[i-2] + abs(heights[i]-heights[i-2])

            dp[i] = min(one, two)

        return dp[n-1]
    
    def frogJumpK(self, heights, k):
        pass
            

sol = Solution()
heights = [2, 1, 3, 5, 4]
print(sol.frogJumps(heights))

            
        