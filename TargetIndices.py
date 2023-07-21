class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        arr=sorted(nums)
        array=[]
        if target not in arr:
            return []
        else:
            for i in range(len(nums)):
                if arr[i] == target:
                    array.append(i)
            return array
          
