class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)
        if len1 > len2:
            return False

        s1_dict = {i: 0 for i in range(26)}
        s2_dict = s1_dict.copy()
        for c in s1:
            s1_dict[ord(c)-97] += 1

        for c in s2[:len1]:
            s2_dict[ord(c)-97] += 1

        if s1_dict == s2_dict:
            return True

        for idx in range(len1, len2):
            # idx refers to the char to add:
            s2_dict[ord(s2[idx-len1])-97] -= 1
            s2_dict[ord(s2[idx])-97] += 1
            if s1_dict == s2_dict:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.checkInclusion('ab', 'dasfjjioab'))
    print(s.checkInclusion('ab', 'jeiwojfioba'))
    print(s.checkInclusion('ab', 'oooooaoboo'))




