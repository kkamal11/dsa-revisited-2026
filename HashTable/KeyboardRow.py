from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        mapp = {1: set("qwertyuiop"), 2: set("asdfghjkl"), 3: set("zxcvbnm")}
        ans = []
        row = 0
        for s in words:
            if s[0].lower() in mapp[1]:
                row = 1
            if s[0].lower() in mapp[2]:
                row = 2
            if s[0].lower() in mapp[3]:
                row = 3
            if row == 0:
                continue
            curr = []
            for ch in s:
                if ch.lower() in mapp[row]:
                    curr.append(ch)
                else:
                    break
            s1 = "".join(curr)
            if s1 == s:
                ans.append(s1)
        return ans


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        mapp = {1: set("qwertyuiop"), 2: set("asdfghjkl"), 3: set("zxcvbnm")}
        ans = []
        row = 0
        for s in words:
            if s[0].lower() in mapp[1]:
                row = 1
            if s[0].lower() in mapp[2]:
                row = 2
            if s[0].lower() in mapp[3]:
                row = 3
            if row == 0:
                continue
            valid = True
            for ch in s:
                if ch.lower() not in mapp[row]:
                    valid = False
                    break
            if valid:
                ans.append(s)
        return ans
