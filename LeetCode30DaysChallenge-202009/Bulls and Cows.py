from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A = sum([secret[idx] == guess[idx] for idx in range(len(secret))])
        secret_dist = Counter(secret)
        guess_dict = Counter(guess)
        B = sum([min(secret_dist[key], guess_dict[key]) for key in secret_dist])
        return str(A) + "A" + str(B - A) + "B"


if __name__ == '__main__':
    s = Solution()
    print(s.getHint(secret="1807", guess="7810"))
    print(s.getHint(secret="1123", guess="0111"))
