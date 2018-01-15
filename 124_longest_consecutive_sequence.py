class Solution:
    """
    @param: num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, nums):
        # write your code here
        num_set = set(nums)
        longest = 0
        for n in nums:
            if n not in num_set:
                pass
            seq_length = 1
            pointer = n - 1
            while pointer in num_set:
                seq_length += 1
                num_set.remove(pointer)
                pointer -= 1
            pointer = n + 1
            while pointer in num_set:
                seq_length += 1
                num_set.remove(pointer)
                pointer += 1
            longest = max(longest, seq_length)
        return longest
