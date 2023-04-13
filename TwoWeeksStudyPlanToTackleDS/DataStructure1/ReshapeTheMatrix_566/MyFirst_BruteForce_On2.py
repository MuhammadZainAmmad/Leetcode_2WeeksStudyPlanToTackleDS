class Solution(object):
    def matrixReshape(self, mat, r, c):

        # MyFirst: Brute Force
        # Time: O(n^2), Space: O(n)

        totalEle = [] # Converting nested list into single list
        for subList in mat:
            for ele in subList:
                totalEle.append(ele)

        if len(totalEle) != r*c:
            return mat
        
        start = 0
        desList = []
        for i in range((len(totalEle)/c)):
            desList.append(totalEle[start:start+c])
            start += c
            print(start)

        return desList