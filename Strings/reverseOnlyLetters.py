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

    def reverseOnlyLetters2(self, s: str) -> str:
        letters = [c for c in s if c.isalpha()]
        result = []

        for c in s:
            if c.isalpha():
                result.append(letters.pop())
            else:
                result.append(c)

        return "".join(result)
