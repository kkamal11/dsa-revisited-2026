class Solution:

    def reverseDegree(self, s: str) -> int:
        reverse_degree = 0

        for idx, ch in enumerate(s):
            reverse_degree += (ord("z") - ord(ch) + 1) * (idx + 1)

        return reverse_degree
