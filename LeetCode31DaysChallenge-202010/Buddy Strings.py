from collections import Counter


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        counter_A = Counter(A)
        counter_B = Counter(B)
        if counter_A != counter_B:
            return False
        diff_places = sum([a != b for a, b in zip(A, B)])
        if diff_places not in [0, 2]:
            return False
        if diff_places == 0 and len(counter_A) == len(A):
            return False
        if diff_places == 2 and len(counter_A) == 1:
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.buddyStrings(A="ab", B="ba"))
    print(s.buddyStrings(A="ab", B="ab"))
    print(s.buddyStrings(A="aa", B="aa"))
    print(s.buddyStrings(A="aaaaaaabc", B="aaaaaaacb"))
    print(s.buddyStrings(A="", B="aa"))
    print(s.buddyStrings(A="aaab", B="aa"))
