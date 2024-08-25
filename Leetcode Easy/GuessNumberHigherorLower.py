#https://leetcode.com/problems/guess-number-higher-or-lower/description/
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lower, higher = 0, n
        while lower <= higher:
            middle = (lower + higher)/2
            if guess(middle) < 0:
                higher = middle - 1
            elif guess(middle) > 0:
                lower = middle + 1
            else:
                return middle
        return -1
        