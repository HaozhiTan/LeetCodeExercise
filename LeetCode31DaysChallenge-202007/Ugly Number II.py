class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # dp
        # ugly number = MIN(L1 * 2, L2 * 3, L3 * 5)
        # can only use the previous ugly number to get new ugly number
        ugly_number = [1]
        no_of_factors = 3
        factors = [2, 3, 5]
        index_of_ugly_number_for_factor = [0, 0, 0]  # refers to the multiples of 2, 3, 5, start with 1, 1, 1
        for i in range(n-1):
            candidate_ugly_number = [factors[j] * ugly_number[index_of_ugly_number_for_factor[j]] for j in range(no_of_factors)]
            new_ugly_number = min(candidate_ugly_number)
            ugly_number.append(new_ugly_number)
            index_of_ugly_number_for_factor = [index_of_ugly_number_for_factor[j] + (candidate_ugly_number[j] == new_ugly_number)
                                    for j in range(no_of_factors)]
        return ugly_number[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.nthUglyNumber(1))
    print(s.nthUglyNumber(10))
    print(s.nthUglyNumber(1690))
