from typing import List
from collections import deque
import string


class Solution:
    def gen_seq_word(self, w):
        words = []
        for i in range(len(w)):
            for ch in string.ascii_lowercase:
                nw = w[:i] + ch + w[i + 1 :]
                words.append(nw)
        return words

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_list = set(wordList)
        used_word_list = set()

        if endWord not in word_list:
            return 0

        q = deque()
        q.append((beginWord, 1))
        used_word_list.add(beginWord)

        while q:
            curr_word, level = q.popleft()

            if curr_word == endWord:
                return level

            all_words = self.gen_seq_word(curr_word)
            for word in all_words:
                if word not in used_word_list and word in word_list:
                    used_word_list.add(word)
                    q.append((word, level + 1))

        return 0


sol = Solution()
word = "dog"
print(sol.gen_seq_word(word))
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(sol.ladderLength(beginWord, endWord, wordList))
