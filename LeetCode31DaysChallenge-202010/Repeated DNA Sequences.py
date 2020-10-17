from typing import List
from collections import Counter


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        count = Counter([s[i-10:i] for i in range(10, len(s) + 1)])
        return [key for key in count if count[key] > 1]