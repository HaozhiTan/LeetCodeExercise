class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # check if all letters in this word are capitals
        upper_word = word.upper()
        if upper_word == word:
            return True
        # check if all letters in this word are not capitals
        lower_word = word.lower()
        if lower_word == word:
            return True
        # Only the first letter in this word is capital, like "Google"
        capital_word = word.capitalize()
        if capital_word == word:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.detectCapitalUse('FlaG'))
    print(s.detectCapitalUse('FLaG'))
    print(s.detectCapitalUse('FLAG'))
    print(s.detectCapitalUse('Flag'))
    print(s.detectCapitalUse('flag'))
