class Solution:
    def countElements(self, arr) -> int:
        arr_set = set(arr)
        count = 0
        for num in arr:
            if num+1 in arr_set:
                count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.countElements([1, 3, 2, 3, 5, 0]))
