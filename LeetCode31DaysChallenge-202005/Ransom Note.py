import collections
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # d = collections.defaultdict(int)
        # ans = True
        # for m in magazine:
        #     d[m] += 1
        # for note in ransomNote:
        #     d[note] -= 1
        #     if d[note] < 0:
        #         ans = False
        #         break
        # return ans
        return all(ransomNote.count(note) <= magazine.count(note) for note in set(ransomNote))


if __name__ == '__main__':
    s = Solution()
    print(s.canConstruct('a', 'b'))
    print(s.canConstruct('aa', 'ab'))
    print(s.canConstruct('aa', 'aab'))
