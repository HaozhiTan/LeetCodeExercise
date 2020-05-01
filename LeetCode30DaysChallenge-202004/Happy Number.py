class Solution:
    def isHappy(self, n: int) -> bool:
        d = {}
        while True:
            num_list = [int(i)**2 for i in str(n)]
            sum_list = sum(num_list)
            if sum_list in d.keys():
                return False
            elif sum_list == 1:
                return True
            else:
                d[n] = sum_list
                n = sum_list


if __name__ == "__main__":
    s = Solution()
    print(s.isHappy(29))
