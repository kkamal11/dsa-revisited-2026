from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mini = maxi = nums[0]
        for num in nums:
            if num > maxi:
                maxi = num
            if num < mini:
                mini = num

        while mini != 0:
            maxi, mini = mini, maxi % mini

        return maxi
