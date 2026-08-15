from collections import Counter
from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        d = Counter(licensePlate.lower())

        ans = ""

        for word in words:
            word_count = Counter(word)
            for w in d:
                if w.isalpha() and word_count[w] < d[w]:
                    break
            else:
                if ans == "":
                    ans = word
                elif len(word) < len(ans):
                    ans = word

        return ans

    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        d = Counter(ch.lower() for ch in licensePlate if ch.isalpha())

        ans = ""

        for word in words:
            wd = Counter(word)
            for w in d:
                if w.isalpha() and (w not in wd or wd[w] < d[w]):
                    break
            else:
                if not ans or len(word) < len(ans):
                    ans = word

        return ans
