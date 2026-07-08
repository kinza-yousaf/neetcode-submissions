class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        self.length = 0

        heapq.heapify(self.minHeap)
        heapq.heapify(self.maxHeap)

        

    def addNum(self, num: int) -> None:
        self.length += 1
        heapq.heappush(self.maxHeap, -num)
        if self.minHeap and -self.maxHeap[0] > self.minHeap[0]:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

        if len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        if len(self.maxHeap) < len(self.minHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.maxHeap) == 0:
            return 0
        elif len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] + -self.maxHeap[0]) / 2
        else:
            return -self.maxHeap[0]


        
        