class Solution:
    # @param {string[]} dict an array of n distinct non-empty strings
    # @return {string[]} an array of minimal possible abbreviations for every word
    def wordsAbbreviation(self, strings):
        # Write your code here
        self.abbrs = {}
        self.solve(strings, 0)
        return map(self.abbrs.get, strings)

    def abbr(self, word, size):
        if len(word) - size <= 3:
            return word
        return word[:size + 1] + str(len(word) - size - 2) + word[-1]

    def solve(self, strings, size):
        dlist = collections.defaultdict(list)
        for word in strings:
            dlist[self.abbr(word, size)].append(word)
        for abbr, wlist in dlist.iteritems():
            if len(wlist) == 1:
                self.abbrs[wlist[0]] = abbr
            else:
                self.solve(wlist, size + 1)
