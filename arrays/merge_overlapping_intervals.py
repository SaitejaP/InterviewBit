# Given a collection of intervals, merge all overlapping intervals.


class Interval:

    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval

    def merge(self, intervals):
        if len(intervals) == 1:
            return intervals
        intervals = [(i.start, i.end) for i in intervals]
        intervals = sorted(intervals)
        intervals = [Interval(i[0], i[1]) for i in intervals]
        res = []
        prev = intervals[0]
        for curr in intervals:
            if curr.start <= prev.end:
                prev.end = max(curr.end, prev.end)
            else:
                res.append(prev)
                prev = curr
        res.append(prev)
        return res

intervals = [(1, 4), (2, 4), (2, 3), (2, 5)]
arr = []
for interval in intervals:
    arr.append(Interval(interval[0], interval[1]))

print Solution().merge(arr)
