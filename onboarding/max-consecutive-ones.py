class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        global_max = 0
        current_max = 0

        for right in range(len(nums)):
            if nums[right] == 1:
                current_max += 1
                global_max = max(global_max, current_max)
            else:
                current_max = 0

        return global_max
