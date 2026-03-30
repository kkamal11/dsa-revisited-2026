from collections import deque


def bfs(adjancy_list):
    n = len(adjancy_list)
    q = deque()
    visited = set()

    nodes = []

    level = 0
    start = 1
    q.append(start)
    visited.add(start)

    while q:
        node = q.popleft()
        nodes.append(node)
        for neighbour in adjancy_list[node]:
            if neighbour not in visited:
                level += 1
                visited.add(neighbour)
                q.append(neighbour)
        level += 1
    return level, nodes


from collections import deque


def bfs_level_wise(adj_list):
    visited = set()
    q = deque()

    q.append(1)
    visited.add(1)

    level = 0
    nodes = []

    while q:
        size = len(q)  # number of nodes at current level
        print(f"Level {level}:", end=" ")
        level += 1
        for _ in range(size):
            node = q.popleft()
            print(node, end=" ")
            nodes.append(node)

            for neighbour in adj_list[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    q.append(neighbour)
        print()

    return level - 1, nodes


adj_list = {
    1: [2, 6],
    2: [1, 3, 4],
    3: [2],
    4: [2, 5],
    5: [4, 7],
    6: [1, 7, 8],
    7: [6],
    8: [6],
}
level, path = bfs(adj_list)
print(f"{level=} {path=}")
level, path = bfs_level_wise(adj_list)
print(f"{level=} {path=}")
