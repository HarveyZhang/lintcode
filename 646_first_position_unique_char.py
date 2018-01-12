class Solution:
    """
    @param: s: a string
    @return: it's index
    """
    def firstUniqChar(self, s):
        # write your code here
        import collections

        char_count = collections.defaultdict(int)
        for c in s:
            char_count[c] += 1

        for i in xrange(len(s)):
            if char_count[s[i]] == 1:
                return i
        return -1
