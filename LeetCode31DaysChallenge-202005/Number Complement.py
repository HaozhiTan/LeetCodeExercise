class Solution:
    def findComplement(self, num: int) -> int:
        # Intuitive way faster
        d = {'0': '1', '1': '0'}
        binary_num = bin(num)
        n = [d[c] for c in binary_num[2:]]
        ans = '0b' + ''.join(n)
        return int(ans, base=2)

        # # 1 xor 0 = 1, 1 xor 1 = 0 slower
        # return num ^ (2**len(bin(num)[2:])-1)


if __name__ == '__main__':
    s = Solution()
    print(s.findComplement(5))
    print(s.findComplement(7))
    print(s.findComplement(10))
    print(s.findComplement(1))
    print(s.findComplement(21343123123))
