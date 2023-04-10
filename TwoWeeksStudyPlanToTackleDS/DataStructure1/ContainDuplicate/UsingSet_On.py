# Solution with set
# Time: O(n), Space: O(1)
class Solution(object): 
    def containsDuplicate(self, nums):
        uniqueNums = set()
        for i in nums:
            if i in uniqueNums: # O(1) searching in set is O(1)
                return True # b/c set already contain the value (duplicate)
            uniqueNums.add(i)
        return False