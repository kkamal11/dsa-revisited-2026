from collections import defaultdict, Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = defaultdict(int)
        b = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}

        for ch in text:
            d[ch] += 1

        count = 0
        can_form = True

        while can_form:
            for k in b:
                if k in d and d[k] >= b[k]:
                    continue
                else:
                    can_form = False
                    break

            if can_form:
                count += 1
                for k in b:
                    d[k] -= b[k]

        return count

    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter(text)

        return min(c["b"], c["a"], c["l"] // 2, c["o"] // 2, c["n"])
