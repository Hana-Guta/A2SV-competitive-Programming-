class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        seen = set()

        for interval in ranges:
            start = interval[0] 
            end = interval[1]

            for i in range(start , end + 1):
                seen.add(i)

        for num in range(left , right + 1):
            if num not in seen:
                return False
        return True
            