class Solution:

    def reverseDegree(self, s: str) -> int:
        reverse_degree = 0

        for idx, ch in enumerate(s):
            reverse_degree += (ord("z") - ord(ch) + 1) * (idx + 1)

        return reverse_degree

    def reverseDegree(self, s: str) -> int:
        reverse_degree = 0
        ord_z = 123
        _ord = ord
        for idx, ch in enumerate(s, 1):
            reverse_degree += (ord_z - _ord(ch)) * idx

        return reverse_degree
