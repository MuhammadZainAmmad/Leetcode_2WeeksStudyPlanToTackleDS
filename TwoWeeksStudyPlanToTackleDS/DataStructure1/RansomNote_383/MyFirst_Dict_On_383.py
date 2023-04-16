class Solution(object):
    def canConstruct(self, ransomNote, magazine):

        # MyFirst: Using Dict
        # Time: O(n), Space: O(n)
        magazineDict = {}
        for char in magazine: # O(n)
            magazineDict.update({char : magazineDict.get(char, 0) + 1})
        
        for char in ransomNote: # O(n)
            if magazineDict.get(char) > 0:
                magazineDict[char] -= 1
            else:
                return False
        return True