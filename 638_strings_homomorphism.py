class Solution:
    """
    @param: s: a string
    @param: t: a string
    @return: true if the characters in s can be replaced to get t or false
    """
    def isIsomorphic(self, s, t):
        # write your code here
        mappings = {}
        reverse = {}
        if s is None or t is None or len(s) != len(t):
            return False
        for idx in xrange(len(s)):
            if s[idx] in mappings and t[idx] != mappings[s[idx]]:
                return False
            elif t[idx] in reverse and s[idx] != reverse[t[idx]]:
                return False
            else:
                mappings[s[idx]] = t[idx]
                reverse[t[idx]] = s[idx]
        return True
