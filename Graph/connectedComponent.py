from collections import defaultdict, deque


def num_of_conn_components(nodes, edges):
    visited = set()
    adj = defaultdict(list)
    count = 0
    q = deque()

    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    for i in range(nodes):
        if i not in visited:
            visited.add(i)
            count += 1
            q.append(i)
            while q:
                u = q.popleft()
                for nbr in adj[u]:
                    if nbr not in visited:
                        visited.add(nbr)
                        q.append(nbr)
    print(visited)
    return count


# V = 7
# edges = [[0, 1], [1, 2], [2, 3], [4, 5]]
V = 4
edges = [[0, 1], [1, 2]]
print(num_of_conn_components(V, edges))
