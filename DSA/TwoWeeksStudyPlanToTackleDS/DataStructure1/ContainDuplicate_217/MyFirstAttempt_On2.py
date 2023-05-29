# My first solution 
# Passing 65/71 test cases (Time limit exceeded)
# Time: O(n^2), Space: O(1)
class Solution(object):
    def containsDuplicate(self, nums):
        for i in nums: # O(n)
            if nums.count(i) > 1: # O(n) 
                return True 
            else:
                continue
        return False
    
