class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        if sum(nums) < target: 
            return 0              
        summ, left, ans = 0, 0, len(nums)                   
        
        for right,val in enumerate(nums):                 
            summ+= val                                   
            while summ >= target:                       
                summ-= nums[left]                           
                ans = min(ans, right - left + 1)           
                left += 1                                 

        return ans                                    
