class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
       
        def sortt(elt):
            if elt in arr2:
                return arr2.index(elt) 
            else:
                return len(arr2) + elt  

        sorted_arr1 = sorted(arr1 , key=sortt)

        return sorted_arr1


 
  
