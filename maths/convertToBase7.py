class Solution:
    def convertToBase7(self, num: int) -> str:
        ans = []
        n = abs(num)
        
        while n > 0:
            rem = n % 7
            ans.append(rem)
            n //= 7
        
        sev = "".join((str(x) for x in reversed(ans)))
        
        return "0" if num == 0 else (sev if num > 0 else "-" + sev)