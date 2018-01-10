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
        distance = abs(len_s - len_t)

        if distance > 1:
            return False
        elif distance == 0:
            one_different = False
            for i in xrange(len_s):
                if s[i] != t[i]:
                    if one_different:
                        return False
                    else:
                        one_different = True
            if not one_different:
                return False
            else:
                return True
        else:
            min_len = min(len_s, len_t)
            for i in xrange(min_len):
                if s[i] != t[i]:
                    if len_s > len_t:
                        return s[i + 1:] == t[i:]
                    else:
                        return s[i:] == t[i + 1:]
            return True
