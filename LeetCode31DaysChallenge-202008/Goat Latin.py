class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        word_list = S.split()
        ans = []
        for idx, word in enumerate(word_list, start=1):
            if word[0].lower() in vowels:
                curr_word = word + 'ma'
            elif word[0].lower() not in vowels:
                curr_word = word[1:] + word[0] + 'ma'
            curr_word = curr_word + idx * 'a'
            ans.append(curr_word)
        return ' '.join(ans)


if __name__ == '__main__':
    s = Solution()
    print(s.toGoatLatin("I speak Goat Latin"))
    print(s.toGoatLatin("The quick brown fox jumped over the lazy dog"))