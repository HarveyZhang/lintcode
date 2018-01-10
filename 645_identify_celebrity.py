"""
The knows API is already defined for you.
@param a, person a
@param b, person b
@return a boolean, whether a knows b
you can call Celebrity.knows(a, b)
"""


class Solution:
    # @param {int} n a party with n people
    # @return {int} the celebrity's label or -1
    def findCelebrity(self, n):
        # Write your code here
        candidate = 0

        for i in xrange(n):
            if Celebrity.knows(candidate, i):
                candidate = i

        for i in xrange(candidate):
            if Celebrity.knows(candidate, i) or \
                not Celebrity.knows(i, candidate):
                return -1

        for i in xrange(candidate + 1, n):
            if not Celebrity.knows(i, candidate):
                return -1

        return candidate
