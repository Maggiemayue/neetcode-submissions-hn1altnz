class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dp -> O(n^2) -> greedy
        n = len(nums)
        if n == 1:
            return True

        target = n-1
        # for i in reversed(range(n-1)):
        for i in range(n-1,-1,-1):
            # CAN jump to or beyond the position
            if i + nums[i] >= target:
                target = i
        return target == 0
