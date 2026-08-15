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
