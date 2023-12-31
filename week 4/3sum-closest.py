class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        diff = float('inf')

        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                summ = nums[i] + nums[right] + nums[left]
                if abs(target - summ) < diff:
                    diff = abs(target - summ)
                    res = summ

                if summ < target:
                    left += 1
                else:
                    right -= 1
        return res



        