from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        in_hand = {5:0, 10:10, 20:0}
        
        for paym in bills:
            if paym == 5:
                in_hand[paym] += 1
            elif paym == 10:
                if in_hand[5] > 0:
                    in_hand[paym] += 1
                    in_hand[5] -= 1
                else:
                    return False
            else:
                if in_hand[10] > 0 and in_hand[5] > 0:
                    in_hand[20] += 1
                    in_hand[10] -=1
                    in_hand[5] -= 1
                elif in_hand[5] >= 3:
                    in_hand[5] -= 3
                else:
                    return False
        return True

sol = Solution()
bills = [5,5,10,10,20]
print(sol.lemonadeChange(bills))
bills = [5,5,5,10,5,5,10,20,20,20]
print(sol.lemonadeChange(bills))
