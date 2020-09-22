from collections import defaultdict

class Solution:
    def majorityElement(self, nums):
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
            if len(d) == 3:
                temp_dict = defaultdict(int)
                for key, value in d.items():
                    if value > 1:
                        temp_dict[key] = value - 1
                d = temp_dict
        return [key for key in d.keys() if nums.count(key) > len(nums) // 3]


if __name__ == '__main__':
    s = Solution()
    print(s.majorityElement([1,1,1,3,3,2,2,2]))
