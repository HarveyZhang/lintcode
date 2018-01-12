"""
The read4 API is already defined for you.
@param buf a list of characters
@return an integer
you can call Reader.read4(buf)
"""


class Solution:
    def __init__(self):
        self.buf4 = [None] * 4
        self.current = 0
        self.end = 0

    # @param {char[]} buf destination buffer
    # @param {int} n maximum number of characters to read
    # @return {int} the number of characters read
    def read(self, buf, n):
        # Write your code here
        i = 0
        while i < n:
            if self.current == self.end:
                self.current, self.end = 0, Reader.read4(self.buf4)
                if not self.end:
                    break
            buf[i] = self.buf4[self.current]
            self.current += 1
            i += 1
        return i
