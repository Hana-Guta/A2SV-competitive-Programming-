class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        changes = 0
        left = 0 
        answer = -1

        for right in range(len(nums)):
            if nums[right] == 0:
                changes += 1
            while changes > k and left < len(nums):
                if nums[left] == 0:
                    changes -= 1
                left += 1

            answer = max(answer , right - left + 1)

        return answer



        