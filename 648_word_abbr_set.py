class ValidWordAbbr:
    """
    @param: dictionary: a list of words
    """
    def __init__(self, dictionary):
        # do intialization if necessary
        from collections import defaultdict
        self.abbr_dict = defaultdict(set)
        self.word_abbr_mapping = {}
        for word in dictionary:
            self.abbr_dict[self.get_abbr(word)].add(word)

    """
    @param: word: a string
    @return: true if its abbreviation is unique or false
    """
    def isUnique(self, word):
        # write your code here
        abbr = self.get_abbr(word)
        if abbr not in self.abbr_dict:
            return True
        return len(self.abbr_dict[abbr]) == 1 and word in self.abbr_dict[abbr]

    def get_abbr(self, word):
        if not word in self.word_abbr_mapping:
            abbr = word
            word_length = len(word)
            if word_length > 2:
                abbr = word[0] + str(word_length - 2) + word[-1]
            self.word_abbr_mapping[word] = abbr
        return self.word_abbr_mapping[word]

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param = obj.isUnique(word)