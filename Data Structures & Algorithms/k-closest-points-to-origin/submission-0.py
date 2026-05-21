import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distanceMap = defaultdict(float)
        for point in points:
            x, y = point
            dist = math.sqrt(x ** 2 + y ** 2)
            distanceMap[(x, y)] = dist
        sortedMap = sorted(distanceMap.items(), key = lambda x: x[1])
        res = []
        for i in range(k):
            res.append(sortedMap[i][0])
        return res