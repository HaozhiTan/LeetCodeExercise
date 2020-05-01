from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        d = defaultdict(list)
        for string in strs:
            letter = [0] * 26
            for char in string:
                letter[ord(char)-ord('a')] += 1
            d[tuple(letter)].append(string)
        return list(d.values())


if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
