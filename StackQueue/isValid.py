class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {"]": "[", "}": "{", ")": "("}

        for ch in s:
            if ch in ["{", "(", "["]:
                stack.append(ch)
            else:
                if not stack:
                    return False
                last = stack.pop()
                if last != pair[ch]:
                    return False

        return len(stack) == 0
