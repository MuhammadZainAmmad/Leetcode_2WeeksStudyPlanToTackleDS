# My first attempt
# Time: O(n^2), Space: O(1)
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len (t):
            return False
        
        for i in s: # O(n)
            if s.count(i) != t.count(i): # O(n)
                return False
            else:
                continue
        return True