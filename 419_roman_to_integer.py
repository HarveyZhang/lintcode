class Solution:
    """
    @param: s: Roman representation
    @return: an integer
    """
    def romanToInt(self, s):
        # write your code here
        r_to_i = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0
        len_s = len(s)
        for i in xrange(len_s):
            if i + 1 < len_s:
                if r_to_i[s[i]] < r_to_i[s[i + 1]]:
                    result += -1 * r_to_i[s[i]]
                else:
                    result += r_to_i[s[i]]
            else:
                result += r_to_i[s[i]]
        return result
