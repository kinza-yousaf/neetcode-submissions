class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnts = defaultdict(int)
        for num in nums:
            cnts[num] += 1

        bucketArr = [[] for _ in range (len(nums) + 1)]
        for num, cnt in cnts.items():
            bucketArr[cnt].append(num)

        print(bucketArr)
        res = []
        for i in range(len(nums), -1, -1):
            for num in bucketArr[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res