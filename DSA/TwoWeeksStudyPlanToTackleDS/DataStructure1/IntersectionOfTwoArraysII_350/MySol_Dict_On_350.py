class Solution(object):
    def intersect(self, nums1, nums2):
        # MySecondAttempt: Using Dictionary
        # Time: O(n), Space: O(n)
        commonElements = []
        dictNums1 = {}
        for i in nums1: # O(n)
            dictNums1.update({i : dictNums1.get(i, 0) + 1}) # O(1)
            # dict.get(i, 0) returns the value corresponding to i if it exists otherwise return 0

        for i in nums2: # O(n)
            if i in dictNums1 and dictNums1[i]>0: # O(1)
                commonElements.append(i)
                dictNums1[i] -= 1
        
        return commonElements