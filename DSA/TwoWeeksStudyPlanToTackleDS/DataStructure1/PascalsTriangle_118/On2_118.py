class Solution(object):
    def generate(self, numRows):

        # From Solution: Brute Force
        # Time: O(n^2), Space: O(n)

        pascal = [[1]*(i+1) for i in range(numRows)] # initializing all sub lists with 1
        for i in range(2, numRows):
            for j in range(1,i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return pascal