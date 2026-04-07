from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        coins.sort()

        total_coins = 0

        while amount > 0 and coins:
            denom = coins.pop()
            count = amount // denom
            amount = amount - denom * count
            total_coins += count

        return total_coins if amount == 0 else -1



sol  =Solution()
coins = [1,3,4]
amount = 6
print(sol.coinChange(coins, amount))

coins = [186,419,83,408] # [83, 186, 408, 419] a= 16
amount = 6249
print(sol.coinChange(coins, amount))