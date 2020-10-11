class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # greedy + stack
        last_occurance = {c: idx for idx, c in enumerate(s)}
        stack = ['a']
        visited = set()

        for idx, c in enumerate(s):
            if c in visited:
                continue
            while c < stack[-1] and idx < last_occurance[stack[-1]]:
                visited.remove(stack.pop())
            stack.append(c)
            visited.add(c)
        return ''.join(stack[1:])


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicateLetters("bcabc"))
    print(s.removeDuplicateLetters("cbacdcbc"))
