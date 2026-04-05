from typing import List


class Solution:
    def sign(self, n):
        if n < 0:
            return -1
        return 1

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            survived = True
            while (
                stack
                and self.sign(ast) == -1
                and self.sign(ast) != self.sign(stack[-1])
            ):
                if abs(ast) > stack[-1]:
                    stack.pop()
                elif abs(ast) == stack[-1]:
                    stack.pop()
                    survived = False
                    break
                else:
                    survived = False
                    break

            if survived:
                stack.append(ast)

        return stack


asteroids = [-2, 1, 1, -1]
sol = Solution()
print(sol.asteroidCollision(asteroids))
