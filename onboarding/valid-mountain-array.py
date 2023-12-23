class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        max_num = arr.index(max(arr))
        
        if max_num == 0 or max_num == len(arr)-1:
            return False
        
        for i in range(max_num):
            if arr[i] >= arr[i+1]:
                return False
            
        for i in range(max_num , len(arr) - 1):
            if arr[i] <= arr[i + 1]:
                return False
        
        return True
        