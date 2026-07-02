class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()
        directions=((0,1),(0,-1),(1,0),(-1,0))
        def dfs(r,c,visit):
            if heights[r][c] in visit:
                return
            visit.add((r,c))
            for dr,dc in directions:
                nr = r + dr
                nc = c + dc
                if nr<0 or nr>=rows or nc<0 or nc>=cols or heights[nr][nc]<heights[r][c]:
                    continue
                if (nr,nc) in visit:
                    continue
                dfs(nr,nc,visit)

        for c in range(cols):

            dfs(0, c, pacific)

        for r in range(rows):

            dfs(r, 0, pacific)


        for c in range(cols):

            dfs(rows - 1, c, atlantic)

        for r in range(rows):

            dfs(r, cols - 1, atlantic)
        ans = []

        for r in range(rows):

            for c in range(cols):

                if (r, c) in pacific and (r, c) in atlantic:

                    ans.append([r, c])

        return ans
            

        

        

        