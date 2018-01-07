class Solution:
    """
    @param: encoded: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def numDecodings(self, encoded):
        if encoded is None or len(encoded) == 0 or encoded[0] == '0':
            return 0

        encoded_len = len(encoded)
        ways = [1] * (encoded_len + 1)

        for idx in xrange(2, encoded_len + 1):
            if encoded[idx - 2 : idx] == '10' or \
                encoded[idx - 2 : idx] == '20':
                ways[idx] = ways[idx - 2]
            elif 10 <= int(encoded[idx - 2 : idx]) <= 26:
                ways[idx] = ways[idx - 1] + ways[idx - 2]
            elif encoded[idx - 1] != '0':
                ways[idx] = ways[idx - 1]
            else:
                # invalid
                return 0

        return ways[-1]
