from collections import deque, defaultdict


def number_of_province(mat):
    adj_list = defaultdict(list)
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i != j and mat[i][j] == 1:
                adj_list[i].append(j)
    print(f"{adj_list=}")

    def dfs(adj, node, visited):
        if node in visited:
            return
        visited.add(node)
        for neig in adj[node]:
            if neig not in visited:
                dfs(adj, neig, visited)

    visited = set()
    nodes = range(len(mat))
    count = 0
    for i in nodes:
        if i not in visited:
            count += 1
            dfs(adj_list, i, visited)
    return count


def num_of_provinces_bfs(mat):
    adj = defaultdict(list)
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                adj[i].append(j)
    print(f"{adj=}")
    count = 0
    q = deque()
    provinces_count = 0
    visited = set()
    provinces = range(len(mat))
    for p in provinces:
        if p not in visited:
            q.append(p)
            visited.add(p)
            provinces_count += 1
            while q:
                node = q.popleft()
                for nbr in adj[node]:
                    if nbr not in visited:
                        visited.add(nbr)
                        q.append(nbr)
    return provinces_count


graph = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# graph = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
print(number_of_province(graph))
print(num_of_provinces_bfs(graph))
