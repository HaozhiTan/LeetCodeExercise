class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = self.manipulate_string(version1)
        v2 = self.manipulate_string(version2)
        if len(v1) > len(v2):
            v2 += [0] * (len(v1) - len(v2))
        elif len(v1) < len(v2):
            v1 += [0] * (len(v2) - len(v1))
        for i in range(len(v1)) :
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
        return 0

    def manipulate_string(self, string):
        lst = string.split('.')
        lst = [int(c) for c in lst]
        while lst and lst[-1] == 0:
            lst.pop()
        return lst


if __name__ == '__main__':
    s = Solution()
    print(s.compareVersion(version1="0.1", version2="1.1"))
    print(s.compareVersion(version1="1.0.1", version2="1"))
    print(s.compareVersion(version1="7.5.2.4", version2="7.5.3"))
    print(s.compareVersion(version1="1.01", version2="1.001"))
    print(s.compareVersion(version1="1.0", version2="1.0.0"))
    print(s.compareVersion(version1="1.2", version2="1.10.0"))
