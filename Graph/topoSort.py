class TopoSort:
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()
        self.stack = []

    def dfs(self, node):
        self.visited.add(node)
        for neighbor in self.graph[node]:
            if neighbor not in self.visited:
                self.dfs(neighbor)
        self.stack.append(node)

    def sort(self):
        for node in self.graph:
            if node not in self.visited:
                self.dfs(node)
        return self.stack[::-1]  # Reverse the stack to get the correct order

    def sort_kahn(self):
        in_degree = {node: 0 for node in self.graph}
        for node in self.graph:
            for neighbor in self.graph[node]:
                in_degree[neighbor] += 1

        queue = [node for node in self.graph if in_degree[node] == 0]
        topo_order = []

        while queue:
            node = queue.pop(0)
            topo_order.append(node)
            for neighbor in self.graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(topo_order) != len(self.graph):
            raise ValueError("Graph has a cycle, topological sort not possible")

        return topo_order

    def __repr__(self):
        return f"TopoSort(graph={self.graph})"

    def __str__(self):
        return f"TopoSort(graph={self.graph})"


# Example usage:
if __name__ == "__main__":
    graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
    topo_sort = TopoSort(graph)
    print(topo_sort.sort())  # Output: ['A', 'C', 'B', 'D'] or ['A', 'B', 'C', 'D']
