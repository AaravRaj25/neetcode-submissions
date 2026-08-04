from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A tree with n nodes must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        # Build an undirected graph
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False      # Cycle detected

            visited.add(node)

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue      # Ignore the edge we came from

                if not dfs(neighbor, node):
                    return False

            return True

        # Start DFS from node 0
        if not dfs(0, -1):
            return False

        # Ensure every node was visited (graph is connected)
        return len(visited) == n