import collections


class Solution:
    def findAnagrams(self, s: str, p: str):
        def check_anagrams(string):
            d = collections.defaultdict(int)
            for c in string:
                d[c] += 1
            return d

        target_dict = check_anagrams(p)
        ans = []
        if len(s) < len(p):
            return ans
        curr_dict = check_anagrams(s[:len(p)])
        if curr_dict == target_dict:
            ans.append(0)
        for idx in range(len(p), len(s)):
            removed_char_idx = idx - len(p)
            curr_dict[s[removed_char_idx]] -= 1
            if curr_dict[s[removed_char_idx]] == 0:
                curr_dict.pop(s[removed_char_idx], None)
            curr_dict[s[idx]] += 1
            if curr_dict == target_dict:
                ans.append(removed_char_idx+1)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findAnagrams("cbaebabacd", "abc"))
    print(s.findAnagrams("abab", "ab"))
