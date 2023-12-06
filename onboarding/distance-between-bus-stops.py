class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        n = len(distance)
        pos_start = start % n
        pos_dest = destination % n
        dist_start = 0
        dist_dest = 0
        
        while pos_start != destination and pos_dest != start:
            dist_start += distance[pos_start]
            dist_dest += distance[pos_dest]
            pos_start = (pos_start + 1) % n
            pos_dest = (pos_dest + 1) % n
            
        if pos_start == destination:
            return dist_start
        return dist_dest
