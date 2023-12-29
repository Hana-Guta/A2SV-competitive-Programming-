class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        operations = 0
        curr_max = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < curr_max:
                curr_max = nums[i]
                operations += i

        return operations
