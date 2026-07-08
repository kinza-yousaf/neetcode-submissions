class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.maxHeap = stones
        heapq.heapify_max(self.maxHeap)

        while len(self.maxHeap) > 1:
            prev = heapq.heappop_max(self.maxHeap)
            cur = heapq.heappop_max(self.maxHeap)
            diff = abs(prev - cur)
            heapq.heappush_max(self.maxHeap, diff)
        return self.maxHeap[0]
        

