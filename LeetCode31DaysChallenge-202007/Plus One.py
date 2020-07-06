class Solution:
    def plusOne(self, digits):
        # intuitive O(n)
        digits = [0] + digits
        current = len(digits) - 1
        while digits[current] == 9:
            digits[current] = 0
            current -= 1
        digits[current] += 1
        if digits[0] > 0:
            return digits
        else:
            return digits[1:]

        # # use python in-built function to change list to number and change back (slower)
        # number = int(''.join(map(str, digits)))
        # number += 1
        # ans = list(map(int, str(number)))
        # return ans


if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([4, 3, 2, 1]))
    print(s.plusOne([1, 2, 3]))
    print(s.plusOne([9]))
