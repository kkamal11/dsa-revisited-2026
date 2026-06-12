class Solution:
    """
    Calculates the sum of beauty of all substrings of a given string.
    The beauty of a string is defined as the difference between the
    maximum and minimum frequency of characters in the string.
    Example:
    Input: s = "aabcb"
    Output: 5
    """

    def beautySum(
        self, s: str
    ) -> int:  # O(n^2 * 26) time complexity, O(26) space complexity
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

    def beautySumOptimized(
        self, s: str
    ) -> int:  # O(n^2) time complexity, O(26) space complexity
        n = len(s)
        beauty = 0
        for i in range(n):
            freq = [0] * 26
            for j in range(i, n):
                freq[ord(s[j]) - ord("a")] += 1
                maxi, mini = max(freq), min([f for f in freq if f > 0])
                beauty += maxi - mini
        return beauty
