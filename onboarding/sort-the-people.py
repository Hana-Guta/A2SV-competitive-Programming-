class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        both = list(zip(names, heights))

        swapped = True
        
        for i in range(n):
            swapped = False

            for j in range(n-i-1):
                if both[j][1] < both[j+1][1]:
                    both[j], both[j+1] = both[j+1], both[j]
                  

        names = [name for name, height in both]
        
        return names
