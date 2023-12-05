class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        N = len(nums)
        arr = []

        for i in range (N // 2):
            freq , val  = nums[2*i] ,nums[2*i+1]
            val2 = [val] * freq
            arr += val2

        return arr


            
        