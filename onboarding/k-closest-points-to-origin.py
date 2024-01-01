class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        ans = []
        
        for i in range(len(points)):
            xi = points[i][0]
            yi = points[i][1]

            euclidean_dis = sqrt(xi**2 +yi**2)

            dist.append((euclidean_dis , points[i]))

        dist.sort()
        # print(dist)

        for j in range(k):
            ans.append(dist[j][1])
        return ans  