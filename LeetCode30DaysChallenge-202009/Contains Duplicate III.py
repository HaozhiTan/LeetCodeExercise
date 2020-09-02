class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        # sorted list and binary search to maintain sliding window
        if k == 0:
            return False
        if t == 0 and len(nums) == len(set(nums)):
            return False
        if len(nums) == 0:
            return False

        if len(nums) <= k:
            temp_nums = nums.copy()
            temp_nums.sort()
            for idx in range(len(nums) - 1):
                if temp_nums[idx + 1] - temp_nums[idx] <= t:
                    return True
            return False

        sorted_list = []
        for idx in range(len(nums)):
            if idx > k:
                # remove the extra num from sorted list
                sorted_list.remove(nums[idx - k - 1])
            # find the correct position and insert nums[idx]
            key = nums[idx]
            start = 0
            end = len(sorted_list) - 1
            while start <= end:
                mid = (start + end) // 2
                if key <= sorted_list[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            sorted_list.insert(start, key)
            # check if there is matched combo
            for idx in range(len(sorted_list) - 1):
                if sorted_list[idx + 1] - sorted_list[idx] <= t:
                    return True
        return False


if __name__ == '__main__':
    s = Solution()
    # print(s.containsNearbyAlmostDuplicate(nums=[1, 2, 3, 1], k=3, t=0))
    # print(s.containsNearbyAlmostDuplicate(nums=[1, 0, 1, 1], k=1, t=2))
    # print(s.containsNearbyAlmostDuplicate(nums=[1, 5, 9, 1, 5, 9], k=2, t=3))
    print(s.containsNearbyAlmostDuplicate([2, 0, -2, 2], 2, 1))
