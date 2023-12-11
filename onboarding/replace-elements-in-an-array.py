class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic_t={}

        for idx, val in enumerate(nums):
            dic_t[val]=idx

        for org , new in operations:
            nums[dic_t[org]] = new
            dic_t[new] = dic_t[org]

        return nums
        