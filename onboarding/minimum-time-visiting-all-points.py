class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0
        
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            
            h_dist = abs(x2 - x1)
            v_dist = abs(y2 - y1)
            
            diag_dist = min(h_dist, v_dist)
            
            total_time += diag_dist + max(h_dist - diag_dist, v_dist - diag_dist)
        
        return total_time
