class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, num1 in enumerate(nums):
            num2 = target - num1
            if num2 in dict:
                return [dict[num2], i]
            dict[num1] = i 
        return []


