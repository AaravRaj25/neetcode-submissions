class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        matrix1 = [[0 for _ in range(n)] for _ in range(n)]
        matrix2 = [[0 for _ in range(n)] for _ in range(n)]  
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix1[i][j] = matrix[j][i]
        for i in range(len(matrix)):
            for j in range(n):
                matrix2[i][j] = matrix1[i][n-j-1]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = matrix2[i][j]