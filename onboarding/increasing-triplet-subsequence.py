class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        min_val = 2**31 - 1
        sec_min_val = 2**31 - 1
        
        for num in nums:
            if num <= min_val:
                min_val = num
            elif num <= sec_min_val:
                sec_min_val = num
            else:
                return True
        
        return False

            

        
            