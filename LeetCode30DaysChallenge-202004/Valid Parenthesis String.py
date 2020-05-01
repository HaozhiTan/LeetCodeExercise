class Solution:
    def checkValidString(self, s: str) -> bool:
        if len(s) == 0:
            return True
        ans = True
        count_star = 0
        count_left_parenthesis = 0
        for c in s:
            if c == '(':
                count_left_parenthesis += 1
            elif c == '*':
                count_star += 1
            elif c == ')':
                if count_left_parenthesis == 0:
                    if count_star == 0:
                        ans = False
                        break
                    else:
                        count_star -= 1
                else:
                    count_left_parenthesis -= 1
        if count_left_parenthesis > 0:
            count_star = 0
            count_right_parenthesis = 0
            for c in reversed(s):
                if c == ')':
                    count_right_parenthesis += 1
                elif c == '*':
                    count_star += 1
                elif c == '(':
                    if count_right_parenthesis == 0:
                        if count_star == 0:
                            ans = False
                            break
                        else:
                            count_star -= 1
                    else:
                        count_right_parenthesis -= 1
        return ans


if __name__ == "__main__":
    ss = Solution()
    print(ss.checkValidString("(**********)))))))))))))))))))))"))
    print(ss.checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*"))
    print(ss.checkValidString("((*)(*()(())())())()()((()())((()))(*"))
    print(ss.checkValidString(")****()"))
    print(ss.checkValidString("(*))"))
    print(ss.checkValidString("(*******("))



