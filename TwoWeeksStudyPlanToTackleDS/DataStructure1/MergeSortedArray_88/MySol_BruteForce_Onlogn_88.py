class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # MySol: Brute Force (Array + Sorting) 
        # Time: O(nlogn), Space: O(1) 
        
        del nums1[m:] # O(n)
        nums1 += nums2
        nums1.sort() # O(nlogn)