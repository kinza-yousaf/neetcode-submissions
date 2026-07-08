class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnts = defaultdict(int)
        for num in nums:
            cnts[num] += 1
        arr = [(-cnt, num) for num, cnt in cnts.items()]
        heapq.heapify(arr)

        res = []
        while k > 0:
            res.append(heapq.heappop(arr)[1])
            k -= 1
        return res