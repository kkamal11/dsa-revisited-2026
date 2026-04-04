class Solution:
    def reverserStack(self, stack, i, j):
        """
        Recursive reverse uses O(n) time and O(n) space due to call stack
        T - O(n/2) = O(n)
        """
        if i >= j:
            return stack

        stack[i], stack[j] = stack[j], stack[i]

        return self.reverserStack(stack, i + 1, j - 1)


stack = []
sol = Solution()
print(sol.reverserStack(stack, 0, len(stack) - 1))
