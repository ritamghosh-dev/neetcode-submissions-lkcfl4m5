class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: (x[1],x[2]))
        heap = []
        for p,s,e in trips:
            while heap and heap[-1][0] <= s:
                a,b = heapq.heappop(heap)
                capacity += b
            if capacity >= p:
                capacity -= p
                heapq.heappush(heap,(e, p))
            else:
                return False
        return True

