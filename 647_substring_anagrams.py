class Solution:
    def is_anagram(self, src_count, target_count):
        for c in target_count:
            if not c in src_count:
                return False
            elif src_count[c] != target_count[c]:
                return False
        return True

    """
    @param: s: a string
    @param: p: a string
    @return: a list of index
    """
    def findAnagrams(self, s, p):
        # write your code here
        from Queue import Queue

        p_length = len(p)
        if not s or len(s) < p_length:
            return []

        s_length = len(s)
        result = []
        queue = Queue()
        src_count, target_count = collections.defaultdict(int), collections.defaultdict(int)
        for c in p:
            target_count[c] += 1

        for i in xrange(s_length):
            queue.put(s[i])
            src_count[s[i]] += 1
            if queue.qsize() == p_length:
                if self.is_anagram(src_count, target_count):
                    result.append(i - p_length + 1)
                src_count[queue.get()] -= 1

        return result
