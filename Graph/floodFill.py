from collections import deque


class Solution:

    def floodFill(self, image, sr, sc, color):

        rows = len(image)
        cols = len(image[0])
        original = image[sr][sc]

        if original == color:
            return image

        q = deque()
        q.append((sr, sc))
        image[sr][sc] = color

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while q:
            row, col = q.popleft()
            for dr, dc in dirs:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if image[nr][nc] == original:
                        image[nr][nc] = color
                        q.append((nr, nc))
        return image

    def floodFill2(self, image, sr, sc, color):

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        org = image[sr][sc]

        if org == color:
            return image

        def dfs(image, r, c):

            if (
                r >= len(image)
                or c >= len(image[0])
                or r < 0
                or c < 0
                or image[r][c] != org
            ):
                return

            image[r][c] = color

            for dr, dc in dirs:
                dr = r + dr
                dc = c + dc
                dfs(image, dr, dc)

        dfs(image, sr, sc)
        return image

    def floodFill2(self, image, sr, sc, color):
        org = image[sr][sc]

        if org == color:
            return image

        def dfs(image, r, c):

            if (
                r >= len(image)
                or c >= len(image[0])
                or r < 0
                or c < 0
                or image[r][c] != org
            ):
                return

            image[r][c] = color

            dfs(image, r + 1, c)
            dfs(image, r - 1, c)
            dfs(image, r, c + 1)
            dfs(image, r, c - 1)

        dfs(image, sr, sc)
        return image


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sol = Solution()
print(sol.floodFill(image, 1, 1, 2))
