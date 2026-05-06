class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        stack = []
        n = len(digits)

        curry = 0
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                sum_1 = digits[i] + 1
                if sum_1 >= 10:
                    curry = sum_1 // 10
                    sum_1 = sum_1 % 10
                stack.append(sum_1)
            else:
                if curry:
                    sum_c = digits[i] + curry
                    curry = 0
                    if sum_c >= 10:
                        curry = sum_c // 10
                        sum_c = sum_c % 10
                    stack.append(sum_c)
                else:
                    stack.append(digits[i])
        if curry:
            stack.append(curry)

        ans = []
        while stack:
            ans.append(stack.pop())
        return ans

    def plusOne2(self, digits):
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits
        return [1] + digits
