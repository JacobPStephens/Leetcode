import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        if len(points) <= 1:
            return 0

        graph = {}
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                p1, p2 = tuple(points[i]), tuple(points[j])
                if p1 not in graph:
                    graph[p1] = []
                if p2 not in graph:
                    graph[p2] = []
                graph[p1].append(p2)
                graph[p2].append(p1)

        visited = set()
        minHeap = [(0, tuple(points[0]))]
        heapq.heapify(minHeap)
        totalCost = 0

        while len(visited) < len(points):
            cost, point = heapq.heappop(minHeap)
            if point in visited:
                continue
            for neighbor in graph[point]:
                dist = abs(neighbor[0] - point[0]) + abs(neighbor[1] - point[1])
                heapq.heappush(minHeap, (dist, neighbor))
            totalCost += cost
            visited.add(point)

        return totalCost
