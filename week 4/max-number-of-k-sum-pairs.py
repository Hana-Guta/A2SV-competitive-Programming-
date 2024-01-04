class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left , right = 0 , len(nums) - 1
        ans = 0

        while left < right:
            summ = nums[left] + nums[right]
            if summ == k:
                left += 1
                right -= 1
                ans += 1
            elif summ < k:
                left += 1
            else:
                right -= 1

        return ans
