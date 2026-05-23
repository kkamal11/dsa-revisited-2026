from typing import List


class Solution:
    def is_palindrome(self, word):
        # return word == word[::-1]
        n = len(word)

        for i in range(n // 2):
            if word[i] != word[n - i - 1]:
                return False

        return True

    def find_palindromic_pair(self, arr: List[str]):
        count = 0
        n = len(arr)

        for i in range(n):
            w1 = arr[i]

            for j in range(i + 1, n):
                w2 = arr[j]
                w = w1 + w2
                if self.is_palindrome(w):
                    count += 1

        return count

    def find_palindromic_pair_optimised(self, arr):
        word_map = {word: i for i, word in enumerate(arr)}
        result = 0

        for i, word in enumerate(arr):

            for j in range(len(word) + 1):

                prefix = word[:j]
                suffix = word[j:]

                if self.is_palindrome(prefix):

                    candidate = suffix[::-1]

                    if (
                        candidate in word_map
                        and word_map[candidate] != i
                        and word_map[candidate] < i
                    ):
                        result += 1

                if j != len(word) and self.is_palindrome(suffix):

                    candidate = prefix[::-1]

                    if (
                        candidate in word_map
                        and word_map[candidate] != i
                        and i < word_map[candidate]
                    ):
                        result += 1

        return result


sol = Solution()
arr = ["ab", "ac", "ba", "ca", "cba", "mno", "nm"]
print(sol.find_palindromic_pair(arr))
print(sol.find_palindromic_pair_optimised(arr))
