class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnts = defaultdict(int)
        for num in nums:
            cnts[num] += 1
        heap = [(-cnt, num) for num, cnt in cnts.items()]
        heapq.heapify(heap) # O(n)
        res = []
        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        return res