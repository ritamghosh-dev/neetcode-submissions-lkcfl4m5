class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [ [(points[i][0])**2 + (points[i][1])**2, points[i][0], points[i][1]] for i in range(len(points))]
        distances.sort(key = lambda x: x[0])
        ans = []
        for i in range(k):
            ans.append([distances[i][1],distances[i][2]])
        return ans 