class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        min_val = 2**31 - 1
        sec_min_val = 2**31 - 1
        
        for num in nums:
            if num > sec_min_val:
                return True
            if num < min_val:
                min_val = num
            if num > min_val:
                sec_min_val = num 
                
        return False

        
    

            

        
            