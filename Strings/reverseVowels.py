class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []

        for ch in s:
            if ch.lower() in {"a", "e", "i", "o", "u"}:
                vowels.append(ch)

        ans = []
        for ch in s:
            if ch.lower() in {"a", "e", "i", "o", "u"}:
                ans.append(vowels.pop())
            else:
                ans.append(ch)

        return "".join(ans)

    def reverseVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u"}

        chars = list(s)
        left, right = 0, len(chars) - 1

        while left < right:
            while left < right and chars[left].lower() not in vowels:
                left += 1

            while left < right and chars[right].lower() not in vowels:
                right -= 1

            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

        return "".join(chars)
