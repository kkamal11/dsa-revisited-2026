class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subs = []
        n = len(s)
        for i in range(n):
            sub = []
            for j in range(i, n):
                sub.append(s[j])
                subs.append("".join(sub))
        
        max_len = 0
        for sub in subs:
            if len(set(sub)) == len(sub):
                max_len = max(max_len, len(sub))

        return max_len
    
    def lengthOfLongestSubstringOptimized(self, s:str) -> int:
        max_len = 0
        left = 0
        seen = set()

        for right in range(len(s)):

            while seen and s[right] in seen:
                seen.discard(s[left])
                left += 1

            max_len = max(max_len, right - left + 1)
            seen.add(s[right])

        return max_len
    
    def lengthOfLongestSubstringOptimized2(self, s:str) -> int:
        seen = {}
        max_len = 0
        left = 0
        
        for right in range(len(s)):
            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]] + 1

            seen[s[right]] = right
            max_len = max(max_len, right - left + 1)
        
        return max_len



sol = Solution()
s = "abcabcbb"
s2= "pwwkew"
"""
seen = ke
left = 3
right = 5
max = 3
"""
print(sol.lengthOfLongestSubstring(s2))
print(sol.lengthOfLongestSubstringOptimized(s2))
print(sol.lengthOfLongestSubstringOptimized2(s2))