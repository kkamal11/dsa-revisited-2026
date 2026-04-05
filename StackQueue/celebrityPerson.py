class Solution:
    def findCelebrity(self, mat):
        row = len(mat)
        
        celebrity = -1

        for i in range(row):
            if sum(mat[i]) == 0:
                celebrity = i
                break
        if celebrity == -1:
            return celebrity
        
        for i in range(row):
            if i != celebrity and mat[i][celebrity] != 1:
                return -1
        
        return celebrity
        
    def findCelebrityOptimized(self, mat):
        n = len(mat)

        candidate = 0
        for i in range(1, n):
            if mat[candidate][i] == 1:
                candidate = i

        for i in range(n):
            if i != candidate:
                if mat[candidate][i] == 1 or mat[i][candidate] == 0:
                    return -1

        return candidate
    

sol = Solution()
M = [ 
    [0, 1, 1, 0], 
    [0, 0, 0, 0], 
    [1, 1, 0, 0], 
    [0, 1, 1, 0] 
]
M2 = [ [0, 1], [1, 0] ]
print(sol.findCelebrity(M))
print(sol.findCelebrity(M2))