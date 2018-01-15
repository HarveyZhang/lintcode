class Solution:
    """
    @param: nums: a sorted integer array
    @param: lower: An integer
    @param: upper: An integer
    @return: a list of its missing ranges
    """
    def findMissingRanges(self, nums, lower, upper):
        # write your code here
        if not nums or upper < nums[0] or lower > nums[-1]:
            return [self.get_range_str(lower, upper)]
        ranges = []
        nums.insert(0, lower - 1)
        nums.append(upper + 1)
        for i in xrange(len(nums) - 1):
            tmp_range = self.get_range_str(nums[i] + 1, nums[i + 1] - 1)
            if tmp_range:
                ranges.append(tmp_range)
        return ranges

    def get_range_str(self, start, end):
        if start > end or start + 1 == end:
            return None
        range_str = ''
        if start == end:
            range_str = str(start)
        else:
            range_str = str(start) + '->' + str(end)
        return range_str
