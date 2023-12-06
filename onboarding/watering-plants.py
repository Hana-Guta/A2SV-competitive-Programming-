class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        new = capacity
     
        if plants[-1] <= new:
            steps += 1
            
        for i in range(len(plants) - 1):
                new -= plants[i]
                steps += 1
                if new < plants[i+1]:
                    steps += 2 *(i+1)
                    new = capacity

        return steps
        