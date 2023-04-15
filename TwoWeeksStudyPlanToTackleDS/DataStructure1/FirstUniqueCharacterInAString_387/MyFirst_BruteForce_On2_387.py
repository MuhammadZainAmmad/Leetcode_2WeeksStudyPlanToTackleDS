class Solution(object):
    def firstUniqChar(self, s):

        # # MyFirst: BruteForce
        # # 83/ 105 test cases passed
        # # Time: O(n^2), Space: O(n)
        uniqueChar = []
        for char in s:
            if s.count(char) == 1:
                uniqueChar.append(char)

        if len(uniqueChar) == 0:
            return -1
        else:
            return s.find(uniqueChar[0])