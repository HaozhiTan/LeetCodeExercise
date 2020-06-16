class Solution:
    def validIPAddress(self, IP: str) -> str:
        if '.' not in IP and ':' not in IP:
            return "Neither"
        if '.' in IP:
            s = IP.split('.')
            if len(s) == 4:
                valid = True
                for c in s:
                    try:
                        num = int(c)
                        if num > 255 or num < 0 or (c[0] == '0' and len(c) > 1) or c[0] == '-':
                            valid = False
                            break
                    except:
                        valid = False
                        break
                if valid:
                    return "IPv4"
        if ':' in IP:
            s = IP.split(':')
            if len(s) == 8:
                valid = True
                for c in s:
                    if len(c) > 4 or len(c) == 0 or c[0] == '-':
                        valid = False
                        break
                    try:
                        _ = int(c, 16)
                    except:
                        valid = False
                        break
                if valid:
                    return "IPv6"
        return "Neither"


if __name__ == '__main__':
    s = Solution()
    print(s.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
    print(s.validIPAddress("2001:0db8:85a3:0::8A2E:0370:7334"))
    print(s.validIPAddress("02001:0db8:85a3:0:0:8A2E:0370:7334"))
    print(s.validIPAddress("172.16.254.1"))
    print(s.validIPAddress("172.16.254.01"))
    print(s.validIPAddress("172.16.254.-0"))
    print(s.validIPAddress("02001:0db8:85a3:0:-0:8A2E:0370:7334"))



