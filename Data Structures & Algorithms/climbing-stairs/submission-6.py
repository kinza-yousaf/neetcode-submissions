class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        res = 1
        while n > 1:
            res = one + two
            one = two
            two = res
            n -= 1
        return res