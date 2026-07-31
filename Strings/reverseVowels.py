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
