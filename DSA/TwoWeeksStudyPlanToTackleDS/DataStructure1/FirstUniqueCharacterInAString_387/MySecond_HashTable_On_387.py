class Solution(object):
    def firstUniqChar(self, s):
        # Time: O(n)
        charCount = {}
        for char in s: # O(n)
            charCount.update({char: charCount.get(char, 0)+1})

        uniqueChar = [char for char in charCount if charCount[char] == 1] # O(n)
        
        lowestIndx = float('inf')
        for unique in uniqueChar: # O(n)
            uniqueIndx = s.find(unique) # O(n^2)
            if uniqueIndx < lowestIndx:
                lowestIndx = uniqueIndx
        
        if len(uniqueChar) == 0:
            return -1
        else:
            return lowestIndx
