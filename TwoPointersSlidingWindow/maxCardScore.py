from typing import List
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        score = 0
        n = len(cardPoints)
        left = 0
        right = n - 1
        cards_taken = 0

        while left <= right:

            cards_taken += 1

            if cardPoints[left] > cardPoints[right]:
                score += cardPoints[left]
                left += 1
            else:
                score += cardPoints[right]
                right -= 1

            if cards_taken == k:
                break
        
        return score




sol = Solution()  
cardPoints = [1,2,3,4,5,6,1]
k = 3
print(sol.maxScore(cardPoints, k))

cardPoints = [2,2,2]
k = 2
print(sol.maxScore(cardPoints, k))

cardPoints = [9,7,7,9,7,7,9]
k = 7
print(sol.maxScore(cardPoints, k))


cardPoints = [100,40,17,9,73,75]
k = 3
print(sol.maxScore(cardPoints, k))


