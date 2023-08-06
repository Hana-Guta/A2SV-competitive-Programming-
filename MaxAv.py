class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        n = len(nums) 

        if n == 0 or n == 1:
            return float(nums[0])
        if n < k:
            return -1
        
        windowSum = sum(nums[:k])
        maxAv = windowSum/k

        for i in range(n - k):
            windowSum = windowSum - nums[i] + nums[i+k]
            maxAv = max(windowSum/k , maxAv)
        
        return maxAv
        
