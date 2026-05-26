class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff] + 1, i + 1]
            prevMap[num] = i
        return [-1,  -1]


                    

        