class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        beauty = 0
        for i in range(n):
            freq = {}
            for j in range(i, n):
                freq[s[j]] = freq.get(s[j], 0) + 1
                values = freq.values()
                maxi, mini = max(values), min(values)
                beauty += maxi - mini
        return beauty
