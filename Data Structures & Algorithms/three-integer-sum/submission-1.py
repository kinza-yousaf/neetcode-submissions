class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            if num > 0:
                continue
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = num * -1
            targetSums = self.targetSum(target, nums[i+1:])
            if targetSums:
                print(targetSums)
                targetSums = [tuple(sorted(targetSum + [num])) for targetSum in targetSums if targetSum]
                res.extend(targetSums)
            
        dedupedRes = list(set(res))
        dedupedRes = [list(el) for el in dedupedRes]
        return dedupedRes
        

    def targetSum(self, target: int, nums: List[List[int]]):
        prevSet = set()
        res = []
        for num in nums:
            diff = target - num
            if diff in prevSet:
                res.append([num, diff])
            prevSet.add(num)
        return res

        