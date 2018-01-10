class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        encoded = []
        for s in strs:
            for c in s:
                if c == ':':
                    encoded.append('::')
                else:
                    encoded.append(c)
            encoded.append(':;')
        return ''.join(encoded)[:-2]

    """
    @param: encoded: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, encoded):
        # write your code here
        decoded = []
        len_str = len(encoded)
        current = []
        i = 0
        while i < len_str:
            if i + 1 < len_str:
                if encoded[i:i+2] == '::':
                    current.append(':')
                    i += 2
                elif encoded[i:i+2] == ':;':
                    decoded.append(''.join(current))
                    current = []
                    i += 2
                else:
                    current.append(encoded[i])
                    i += 1
            else:
                current.append(encoded[i])
                decoded.append(''.join(current))
                i += 1
        return decoded
