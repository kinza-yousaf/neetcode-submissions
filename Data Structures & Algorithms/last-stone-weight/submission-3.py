class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            prev = heapq.heappop_max(stones)
            cur = heapq.heappop_max(stones)
            if prev - cur > 0:
                heapq.heappush_max(stones, prev - cur)
        return stones[0] if stones else 0
        

