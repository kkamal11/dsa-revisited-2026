class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l = list(s)
        n = len(l)

        left = 0
        right = n - 1

        while left < right:
            if not l[left].isalpha():
                left += 1
                continue
            if not l[right].isalpha():
                right -= 1
                continue

            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1

        return "".join(l)
