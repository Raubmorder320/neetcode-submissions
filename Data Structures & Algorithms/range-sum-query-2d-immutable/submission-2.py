class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.pref_sum = [[0]* len(self.matrix[0]) for _ in range(len(self.matrix))]
        self.pref_sum[0][0] = matrix[0][0]
        for j in range(1,len(self.pref_sum[0])):
            self.pref_sum[0][j] = matrix[0][j]+self.pref_sum[0][j-1]
        for i in range(1, len(self.pref_sum)):
            self.pref_sum[i][0] = matrix[i][0]+ self.pref_sum[i-1][0]
        for i in range(1,len(self.pref_sum)):
            for j in range(1,len(self.pref_sum[0])):
                self.pref_sum[i][j] = matrix[i][j] + self.pref_sum[i-1][j] + self.pref_sum[i][j-1] - self.pref_sum[i-1][j-1]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1==0 and col1==0:
            return self.pref_sum[row2][col2]
        elif row1==0:
            s = self.pref_sum[row2][col2] - self.pref_sum[row2][col1-1]
        elif col1==0:
            s = self.pref_sum[row2][col2] - self.pref_sum[row1-1][col2]
        else:
            s = self.pref_sum[row2][col2] - self.pref_sum[row2][col1-1]-self.pref_sum[row1-1][col2]+self.pref_sum[row1-1][col1-1]
        return s
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)