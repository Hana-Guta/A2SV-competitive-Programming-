class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        same_num = {num for i , num in enumerate(fronts) if backs[i] == num}
        combined = fronts + backs

        minn = 2001
        
        for num in combined:
            if num not in same_num:
                minn = min(minn , num)
            if minn != 2001:
                result = minn
            else:
                result = 0

        return result

           
        return 0
            
       