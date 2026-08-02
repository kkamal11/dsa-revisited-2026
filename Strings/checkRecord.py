class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 0

        for ch in s:
            if ch == "A":
                absent += 1

        if "LLL" in s or absent >= 2:
            return False

        return True
