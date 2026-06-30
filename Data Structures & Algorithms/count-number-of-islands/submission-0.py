class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        visited=[[False]*cols for _ in range(rows)]
        def dfs(r,c):
            if r<0 or r>rows-1 or c<0 or c>cols-1:
                return
            if grid[r][c]=="0" or visited[r][c]:
                return
            visited[r][c]=True
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
        
        islands = 0

        for r in range(rows):

            for c in range(cols):

                if grid[r][c] == "1" and not visited[r][c]:

                    islands += 1

                    dfs(r, c)

        return islands
