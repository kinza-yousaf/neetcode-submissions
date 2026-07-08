class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = [ (((x ** 2) + (y ** 2)) ** (1/2), x, y) for x, y in points]
        heapq.heapify(dists)
        res = []
        while k > 0:
            res.append(heapq.heappop(dists))
            k -= 1
        return [[x, y] for dist, x, y in res]
        