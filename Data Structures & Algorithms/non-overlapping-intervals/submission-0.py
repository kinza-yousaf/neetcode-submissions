class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        prevEnd = intervals[0][1]
        res = 0
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < prevEnd:
                res += 1
            else:
                prevEnd = end
        return res