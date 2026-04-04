from typing import List


class Solution:
    def backtrack(self, res, current, open_count, close_count, max_pairs):
        if len(current) == 2 * max_pairs:
            res.append(current)
            return

        if open_count < max_pairs:
            self.backtrack(res, current + "(", open_count + 1, close_count, max_pairs)

        if close_count < open_count:
            self.backtrack(res, current + ")", open_count, close_count + 1, max_pairs)

    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.backtrack(res, "", 0, 0, n)
        return res


sol = Solution()
n = 3
print(sol.generateParenthesis(n))
