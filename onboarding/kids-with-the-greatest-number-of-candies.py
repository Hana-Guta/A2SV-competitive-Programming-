class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        arr = []
        
        for candy in candies:
            if candy + extraCandies >= max(candies):
                arr.append(True)
            else:
                arr.append(False)
        return arr

        