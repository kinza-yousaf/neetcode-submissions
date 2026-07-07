class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newS, newE = newInterval
        res = []

        i = 0
        while i < len(intervals) and newS > intervals[i][1]:
            res.append(intervals[i])
            i += 1
        
        mergedS, mergedE = newS, newE
        while i < len(intervals) and intervals[i][0] <= newE:
            mergedS = min(mergedS, intervals[i][0])
            mergedE = max(mergedE, intervals[i][1])
            i += 1
        res.append([mergedS, mergedE])
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        
        return res
        

