class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum_ = 0

        for i in range(1, num):
            if num % i == 0:
                sum_ += i

        return num == sum_

    """
    
    
    """

    def checkPerfectNumber(self, num: int) -> bool:
        pass
