class Solution:
    """
    @param: inputString: an abstract file system
    @return: return the length of the longest absolute path to file
    """
    def lengthLongestPath(self, inputString):
        # write your code here
        path_len = {0: 0}
        max_len = 0

        for line in inputString.splitlines():
            name = line.lstrip('\t')
            depth = len(line) - len(name)

            if '.' in name: # a file
                max_len = max(max_len, path_len[depth] + len(name))
            else:
                path_len[depth + 1] = path_len[depth] + len(name) + 1

        return max_len
