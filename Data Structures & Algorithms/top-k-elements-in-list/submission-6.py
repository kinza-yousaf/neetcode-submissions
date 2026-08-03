class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnts = defaultdict(int)
        for num in nums:
            cnts[num] += 1
        heap = []
        for num, cnt in cnts.items():
            heapq.heappush(heap, (cnt, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [i[1] for i in heap]