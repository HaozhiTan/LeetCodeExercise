# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        # rejection sampling to use rand7() twice to generate 1 to 49 uniformly
        while True:
            row = rand7()
            column = rand7()
            index = (row - 1) * 7 + column
            if index > 40:
                break
        return (index - 1) % 10 + 1  # return 1 to 10
