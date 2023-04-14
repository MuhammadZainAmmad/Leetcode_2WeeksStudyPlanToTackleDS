class Solution(object):
    def searchMatrix(self, matrix, target):

        # MyFirst: BruteForce
        # Time: O(n^2), Space: O(n)
        allEle = []
        for sub in matrix: 
            allEle.extend(sub)
        
        if target in allEle:
            return True
        else:
            return False