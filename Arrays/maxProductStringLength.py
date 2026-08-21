from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        n = len(words)

        for i in range(n):
            w1 = words[i]
            for j in range(i + 1, n):
                w2 = set(words[j])
                for k in w1:
                    if k in w2:
                        break
                else:
                    ans = max(ans, len(w1) * len(words[j]))
        return ans

    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        n = len(words)
        sets = [set(word) for word in words]

        for i in range(n):
            w1 = words[i]
            for j in range(i + 1, n):
                for k in w1:
                    if k in sets[j]:
                        break
                else:
                    ans = max(ans, len(w1) * len(words[j]))
        return ans

    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        n = len(words)
        sets = [set(word) for word in words]

        for i in range(n):
            for j in range(i + 1, n):
                if sets[i].isdisjoint(sets[j]):
                    ans = max(ans, len(words[i]) * len(words[j]))

        return ans

    def maxProduct(self, words: List[str]) -> int:
        n = len(words)

        masks = []

        for word in words:
            mask = 0

            for ch in word:
                mask |= 1 << (ord(ch) - ord("a"))

            masks.append(mask)

        ans = 0

        for i in range(n):
            for j in range(i + 1, n):
                if masks[i] & masks[j] == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))

        return ans
