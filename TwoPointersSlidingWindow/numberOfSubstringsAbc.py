class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)

        for i in range(n):
            sub = ""
            freq = {"a":0, "b":0, "c":0}
            for j in range(i,n):
                sub += s[j]
                freq[s[j]] = 1

                if freq["a"] == 1 and freq["b"] == 1 and freq["c"] == 1:
                    count += 1

        return count

    def numberOfSubstrings2(self, s: str) -> int:
        count = 0
        n = len(s)

        for i in range(n):
            sub = ""
            freq = {"a":0, "b":0, "c":0}
            for j in range(i,n):
                sub += s[j]
                freq[s[j]] = 1

                if freq["a"] == 1 and freq["b"] == 1 and freq["c"] == 1:
                    count += (n - j)
                    break
                    
        return count
    
    def numberOfSubstringsOptimized(self, s: str) -> int:
        pass


sol = Solution()                
s = "abcabc"
print(sol.numberOfSubstrings(s))
print(sol.numberOfSubstrings2(s))
