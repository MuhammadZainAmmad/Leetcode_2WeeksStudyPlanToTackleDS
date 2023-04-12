class Solution(object):
    def intersect(self, nums1, nums2):

        # MyFirstAttempt: BruteForce
        # Passing 30/56 test cases
        # Time: O(n^2), Space: O(n)
        commonElements = []
        for i in nums1:
            for j in nums2:
                if i == j:
                    commonElements.append(i)
                    break
        return commonElements