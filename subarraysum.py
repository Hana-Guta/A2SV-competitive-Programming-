class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_sum_count = {0: 1}
        
        for num in nums:
            prefix_sum += num
            
            # Check if there is a prefix sum such that prefix_sum - cumulative_sum = k
            # This means the subarray between that prefix sum and the current index has a sum of k
            if prefix_sum - k in prefix_sum_count:
                count += prefix_sum_count[prefix_sum - k]
            
            # Update the count of the current prefix sum in the dictionary
            prefix_sum_count[prefix_sum] = prefix_sum_count.get(prefix_sum, 0) + 1
        
        return count
