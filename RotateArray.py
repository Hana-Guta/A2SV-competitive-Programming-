class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """  
        k = k % len(nums)
        def swap(arr , x , y):
            temp = arr[x]
            arr[x] = arr [y]
            arr[y] = temp
        def twoPointer(arr, start, end ):
            while (start < end):
                swap(arr ,start , end)
                start += 1
                end -= 1
            return arr   
        
        twoPointer(nums, 0, len(nums) - 1)  
        twoPointer(nums, 0, k - 1)          
        twoPointer(nums, k, len(nums) - 1)  
