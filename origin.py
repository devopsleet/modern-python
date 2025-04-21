class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) <= k:
            return points

        heap = []

        for point in points:
            x,y = point

            dist = math.sqrt((x**2) + (y**2))

            if len(heap) < k:
                heapq.heappush(heap, (-dist, point))
            else:
                if -dist > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap,(-dist, point))

        return[point for dist,point in heap ]
