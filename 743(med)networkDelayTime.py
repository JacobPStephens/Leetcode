from collections import deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    
        # source node: (target node, weight)
        graph = {}
        for edge in times:
            source, target, t = edge
            if source not in graph:
                graph[source] = []
            if target not in graph:
                graph[target] = []
            graph[source].append((target, t))

        # queue of nodes
        queue = collections.deque([k])
        mins = {k: 0}

        while queue:
            node = queue.popleft()
            for edge in graph[node]:
                neighbor, t = edge
                newTime = mins[node] + t
                if (neighbor not in mins) or (newTime < mins[neighbor]):
                    mins[neighbor] = newTime
                    queue.append(neighbor)

        if len(mins) != n:
            return -1
        
        return max(mins.values())
