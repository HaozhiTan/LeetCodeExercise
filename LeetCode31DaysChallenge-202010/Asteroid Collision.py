from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # stack
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] > -asteroid:
                    break
                elif stack[-1] == -asteroid:
                    stack.pop()
                    break
                else:
                    stack.pop()
                    continue
            else:
                stack.append(asteroid)
        return stack


if __name__ == '__main__':
    s = Solution()
    print(s.asteroidCollision([5, 10, -5]))
    print(s.asteroidCollision([5, -5]))
    print(s.asteroidCollision([10, 2, -5]))
    print(s.asteroidCollision([-2, -1, 1, 2]))
    print(s.asteroidCollision([2, 1, -1, -2]))
    print(s.asteroidCollision([-2, -2, 1, -2]))