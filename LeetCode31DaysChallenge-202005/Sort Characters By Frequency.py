import collections

class Solution:
    def frequencySort(self, s: str) -> str:
        # d = collections.Counter(s)
        # s_list = [k*v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)]
        # return ''.join(s_list)
        return ''.join(k * v for k, v in collections.Counter(s).most_common())


if __name__ == '__main__':
    s = Solution()
    print(s.frequencySort('tree'))
    print(s.frequencySort('Aabb'))
    print(s.frequencySort('cccaaa'))
