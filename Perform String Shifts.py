class Solution:
    def stringShift(self, s: str, shift) -> str:
        count = 0
        len_str = len(s)
        for action in shift:
            if action[0] == 0:
                count -= action[1]
            elif action[0] == 1:
                count += action[1]
        count = count % len_str
        return s[-count:] + s[:-count]


if __name__ == "__main__":
    ss = Solution()
    print(ss.stringShift(s='abc', shift=[[0, 1], [1, 2]]))
    print(ss.stringShift(s='abcdefg', shift=[[1, 1], [1, 1], [0, 2], [1, 3]]))
    print(ss.stringShift(s="xqgwkiqpif",
                         shift=[[1, 4], [0, 7], [0, 8], [0, 7], [0, 6], [1, 3], [0, 1], [1, 7], [0, 5], [0, 6]]))
