class Solution:
    def sequentialDigits(self, low: int, high: int):
        len_low = len(str(low))
        len_high = len(str(high))
        ans = []
        for digits in range(len_low, len_high + 1):
            for start in range(1, 10 - digits + 1):
                num_list = [str(start + i) for i in range(digits)]
                if low <= int(''.join(num_list)) <= high:
                    ans.append(int(''.join(num_list)))
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.sequentialDigits(1000, 30000))
    print(s.sequentialDigits(1000, 3000))
