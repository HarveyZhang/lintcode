class Solution:
    """
    @param: word: a non-empty string
    @param: abbr: an abbreviation
    @return: true if string matches with the given abbr or false
    """
    def validWordAbbreviation(self, word, abbr):
        # write your code here
        if abbr == '':
            return False

        idx_word = idx_abbr = 0
        len_word = len(word)
        len_abbr = len(abbr)
        while idx_word < len_word and idx_abbr < len_abbr:
            if abbr[idx_abbr] == '0':
                break

            n_digit = 0
            while idx_abbr + n_digit < len_abbr and \
                abbr[idx_abbr + n_digit].isdigit():
                n_digit += 1

            if n_digit > 0:
                idx_word += int(abbr[idx_abbr : idx_abbr + n_digit])
                idx_abbr += n_digit
            elif word[idx_word] == abbr[idx_abbr]:
                idx_word += 1
                idx_abbr += 1
            else:
                break

        return idx_word == len_word and idx_abbr == len_abbr
