class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count_zeros = nums.count(0)
        count_ones = nums.count(1)
        
        max_score = -1
        result = []

        zeros_left = 0
        ones_right = count_ones

        for i in range(n + 1):
            current_score = zeros_left + ones_right

            if current_score > max_score:
                max_score = current_score
                result = [i]
            elif current_score == max_score:
                result.append(i)

            if i < n:
                if nums[i] == 0:
                    zeros_left += 1
                else:
                    ones_right -= 1

        return result

