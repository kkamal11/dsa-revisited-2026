from typing import List


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        ans = []
        part1, part2 = s.split(":")
        c1, r1 = part1
        c2, r2 = part2

        r1, r2 = int(r1), int(r2)
        c1 = ord(c1) - ord("A")
        c2 = ord(c2) - ord("A")

        for j in range(c1, c2 + 1):
            for i in range(r1, r2 + 1):
                cell = f"{chr(65 + j)}{i}"
                ans.append(cell)

        return ans


sol = Solution()
s = "A1:F1"
print(sol.cellsInRange(s))
