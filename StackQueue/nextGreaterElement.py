from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums1)):
            nxt_grt = -1
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    for k in range(j + 1, len(nums2)):
                        if nums2[k] > nums2[j]:
                            nxt_grt = nums2[k]
                            break
                    break
            ans.append(nxt_grt)

        return ans

    def nextGreaterElementOptimized(
        self, nums1: List[int], nums2: List[int]
    ) -> List[int]:
        stack = []
        next_greater = {}

        n = len(nums2)
        for idx in range(n - 1, -1, -1):
            num = nums2[idx]

            while stack and stack[-1] <= num:
                stack.pop()

            if stack == []:
                next_greater[num] = -1
            else:
                next_greater[num] = stack[-1]

            stack.append(num)

        return [next_greater[num] for num in nums1]

    def nextGreaterElementII(self, nums: List[int]) -> List[int]:
        stack = []
        next_greater = {}

        n = len(nums)
        for idx in range(2 * n - 1, -1, -1):
            num = nums[idx % n]

            while stack and stack[-1] <= num:
                stack.pop()

            if stack == []:
                next_greater[num] = -1
            else:
                next_greater[num] = stack[-1]

            stack.append(num)

        return [next_greater[num] for num in nums]


sol = Solution()
n1 = [1, 3, 5, 2, 4]
n2 = [6, 5, 4, 3, 2, 1, 7]
n1 = [1, 2, 4]
n2 = [1, 2, 3, 4]
print(sol.nextGreaterElement(n1, n2))
print(sol.nextGreaterElementOptimized(n1, n2))
