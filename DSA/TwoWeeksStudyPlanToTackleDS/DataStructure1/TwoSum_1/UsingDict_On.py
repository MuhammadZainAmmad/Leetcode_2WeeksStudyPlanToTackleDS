class Solution(object):
    def twoSum(self, nums, target):
        # From Solutions (Tech Wired): Using Dict
        # Time: O(n), Space: O(n)
        
        rem_dict = {} # element : element's index
        for i, j in enumerate(nums):
            # i = index, j = element
            rem = target - j # remainder
            if rem in rem_dict:
                # b/c if remainder exists in nums then
                # the sum of remainder and element would 
                # add up to taget ele + rem = target
                return [i, rem_dict[rem]]
            else: 
                rem_dict[j] = i # element : element's index