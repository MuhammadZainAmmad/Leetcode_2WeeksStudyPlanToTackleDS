class Solution(object):
    def maxProfit(self, prices):

        # MyFirstSol: BruteForce
        # Passed 153/211 test cases
        # Time: O(n), Space: O(1)
        smallestNoIndx = 0
        for i in range(len(prices)):
            if prices[i] < prices[smallestNoIndx]:
                smallestNoIndx = i

        highestPrice = 0
        if smallestNoIndx == len(prices)-1: # i.e. last index
            return 0
        else:
            for i in range(smallestNoIndx+1, len(prices)):
                if prices[i] > highestPrice:
                    highestPrice = prices[i]

        return highestPrice - prices[smallestNoIndx]