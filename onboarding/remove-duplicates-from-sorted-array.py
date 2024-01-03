class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = count = 0

        for right in range(1 ,len(nums)):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
            else:
                count += 1

        return len(nums) - count

        