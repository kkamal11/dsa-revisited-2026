class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []

        for ch in s:
            if ch == "#":
                if s_stack:
                    s_stack.pop()
            else:
                s_stack.append(ch)

        for ch in t:
            if ch == "#":
                if t_stack:
                    t_stack.pop()
            else:
                t_stack.append(ch)

        # return len(s_stack) == len(t_stack) and s_stack == t_stack
        return (
            s_stack == t_stack
        )  # This internally compares the length first and then each element
