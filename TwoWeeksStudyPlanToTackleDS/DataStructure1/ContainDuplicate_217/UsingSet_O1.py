# Time: O(1), Space: O(1)
class Solution(object): 
    def containsDuplicate(self, nums):
        uniqueNums = set(nums)
        if len(uniqueNums) == len(nums): # O(1)
            return False # b/c if duplicate then lengths would not be equal
        else:
            return True