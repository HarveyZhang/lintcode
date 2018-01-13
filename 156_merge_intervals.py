class Solution:
    """
    @param: intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # write your code here
        if not intervals:
            return intervals

        intervals = sorted(intervals, key=lambda interval: interval.start)
        result = [intervals[0]]
        for i in xrange(1, len(intervals)):
            interval = intervals[i]
            if interval.start <= result[-1].end:
                result[-1].end = max(interval.end, result[-1].end)
            else:
                result.append(interval)

        return result
