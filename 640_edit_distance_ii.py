class Solution:
    """
    @param: s: a string
    @param: t: a string
    @return: true if they are both one edit distance apart or false
    """
    def isOneEditDistance(self, s, t):
        # write your code here
        len_s = len(s)
        len_t = len(t)

        if len_s < len_t:
            return self.isOneEditDistance(t, s)

        if len_s - len_t > 1:
            return False

        for i in xrange(len_t):
            if s[i] != t[i]:
                if len_s == len_t:
                    return s[i + 1:] == t[i + 1:]
                else:
                    return s[i + 1:] == t[i:]

        return len_s != len_t
