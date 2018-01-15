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
        new_nums = [lower - 1]
        for num in nums:
            if lower <= num <= upper:
                new_nums.append(num)
        new_nums.append(upper + 1)
        for i in xrange(len(new_nums) - 1):
            tmp_range = self.get_range_str(new_nums[i] + 1, new_nums[i + 1] - 1)
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
