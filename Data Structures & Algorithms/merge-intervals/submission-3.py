class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        lastS, lastE = intervals[0]
        res = []
        
        for i in range(1, len(intervals)):
            interval = intervals[i]
            start, end = interval
            if lastE >= start:
                lastE = max(end, lastE)
            else:
                res.append([lastS, lastE])
                lastS, lastE = start, end
        res.append([lastS, lastE])
        return res