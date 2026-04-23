from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        graph = {i: [] for i in range(numCourses)}

        for u, v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1

        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        topo = []

        while q:
            node = q.popleft()
            topo.append(node)

            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if len(topo) != numCourses:
            return False
        return True
